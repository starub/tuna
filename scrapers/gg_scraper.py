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
import traceback
import urllib

import bs4
import fake_useragent

import config.config as cfg
import entities.match
import entities.opponent


class GGScraper:
    def __init__(self, part):
        self.root_url = cfg.TUNA_CONFIG.get('GOSU_GAMERS', 'url')
        self.sub_url = '/' + part + cfg.TUNA_CONFIG.get('GOSU_GAMERS', 'prefix')
        self.scraper = part
        self.ua = fake_useragent.UserAgent()
        self.logger = cfg.getLogger(__name__ + '.' + part)


    def get_matches(self, div):
        table = div.find('table', {'class': 'simple matches'})

        if table is not None:
            trs = table.find_all('tr')

            with concurrent.futures.thread.ThreadPoolExecutor(max_workers=len(trs)) as executor:
                return list(executor.map(self.parse_tr, trs))


    def parse_tr(self, tr):
        a = tr.find('a', {'class': 'match'})

        html = self.get_html(self.root_url + a['href'])

        if html is None:
            return None

        match = entities.match.Match()

        match.title = html.fieldset.a.text.strip()

        match.stage = html.fieldset.label.text.strip()

        timeTag = html.find('div', {'class': 'match-extras'}).find('p', {'class': 'datetime'})
        if timeTag is not None:
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

        return match


    def get_html(self, url):
        ua = self.ua.random

        headers = {'User-Agent': ua, 'Referer': url, 'Pragma': 'no-cache'}

        req = urllib.request.Request(url, None, headers)

        self.logger.info('requesting {0}'.format(url))

        try:

            response = urllib.request.urlopen(req)
            raw = response.read()
            response.close()

            return bs4.BeautifulSoup(raw);

        except:
            self.logger.error('exception requesting {0}'.format(url))
            traceback.print_exc()


    def scrape(self):
        url = self.root_url + self.sub_url

        self.logger.info('start scraping {0}'.format(url))

        html = self.get_html(url)

        if html is None:
            return None

        divs = html.find('div', id='col1').find_all('div', {'class': 'box'})

        # 1 - Live Matches
        # 2 - Upcoming Matches

        self.logger.info('getting live matches...')
        live_matches = self.get_matches(divs[0])

        self.logger.info('getting upcoming matches...')
        upcoming_matches = self.get_matches(divs[1])

        self.logger.info('done scraping')

        return {
            'timestamp': time.time(),
            'scrapers': self.scraper,
            'live': live_matches if live_matches is not None else [],
            'upcoming': upcoming_matches if upcoming_matches is not None else []
        }
        
