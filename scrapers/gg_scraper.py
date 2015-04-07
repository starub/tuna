'''

Copyright (C) 2015 Stanislavs Rubens (starub_at_protonmail_dot_ch)

This program is free software; you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation; either version 2 of the License, or
(at your option) any later version.
This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
GNU General Public License for more details.
You should have received a copy of the GNU General Public License along
with this program; if not, write to the Free Software Foundation, Inc.,
51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.

'''

import concurrent.futures.thread
import time

import config.config as cfg
import entities.match
import entities.opponent
import entities.event
import scrapers.base_scraper as scraper

class GGScraper(scraper.BaseScraper):
    
    def __init__(self, part):
        super().__init__()
        self.root_url = cfg.TUNA_CONFIG.get('GOSU_GAMERS', 'url')
        self.sub_url = '/' + part + cfg.TUNA_CONFIG.get('GOSU_GAMERS', 'prefix')
        self.scraper = part
        self.logger = cfg.get_logger(__name__ + '.' + part)

    def get_events(self, div):
        table = div.find('table', {'class': 'simple matches'})

        if table:
            trs = table.find_all('tr')

            with concurrent.futures.thread.ThreadPoolExecutor(max_workers=len(trs)) as executor:
                return list(executor.map(self.parse_tr, trs))


    def parse_tr(self, tr):
        a = tr.find('a', {'class': 'match'})

        html = super(GGScraper, self).get_html(self.root_url + a['href'])

        if not html:
            return None

        event = entities.event.Event()
        event.title = html.fieldset.a.text.strip()

        match = entities.match.Match()
        match.title = html.fieldset.a.text.strip()
        match.stage = html.fieldset.label.text.strip()

        timeTag = html.find('div', {'class': 'match-extras'}).find('p', {'class': 'datetime'})
        
        if timeTag:
            event.time = timeTag.text.strip()
            match.time = timeTag.text.strip()

        match.bestof = html.find('div', {'class': 'match-extras'}).find('p', {'class': 'bestof'}).text.strip()

        opponent1 = entities.opponent.Opponent()

        opponent1.name = html.find('div', {'class': 'opponent1'}).h3.text.strip()
        opponent1.rank = html.find('div', {'class': 'opponent1'}).p.text.strip()

        opponent2 = entities.opponent.Opponent()

        opponent2.name = html.find('div', {'class': 'opponent2'}).h3.text.strip()
        opponent2.rank = html.find('div', {'class': 'opponent2'}).p.text.strip()

        match.opponent1 = opponent1
        match.opponent2 = opponent2

        event.matches.append(match)

        return event

    def scrape(self):
        url = self.root_url + self.sub_url

        self.logger.info('start scraping {0}'.format(url))

        html = super(GGScraper, self).get_html(url)

        if not html:
            return None

        divs = html.find('div', id='col1').find_all('div', {'class': 'box'})

        # 0 - Live Matches
        # 1 - Upcoming Matches

        self.logger.info('getting live events...')
        live_events = self.get_events(divs[0])

        self.logger.info('getting upcoming events...')
        upcoming_events = self.get_events(divs[1])

        self.logger.info('done scraping')

        return {
            'timestamp': time.time(),
            'scraper': self.scraper,
            'live': live_events if live_events is not None else [],
            'upcoming': upcoming_events if upcoming_events is not None else []
        }
        
