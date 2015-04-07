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

import datetime

import config.config as cfg
import entities.event
import entities.match
import entities.opponent
import scrapers.base_scraper as scraper


class TLScraper(scraper.BaseScraper):
    
    def __init__(self):
        super().__init__()
        self.logger = cfg.get_logger(__name__)
   
    def scrape(self):
        
        now = datetime.date.today()

        rootUrl = 'http://www.teamliquid.net/calendar/{}/{}/?tourney=16'.format(now.year, now.strftime('%m'))

        html = super(TLScraper, self).get_html(rootUrl)
        
        tables = html.find('div', id='calendar_{}content'.format(now.day)).find_all('table')
       
        events = []
        
        for table in tables:
            
            event = entities.event.Event()
            
            event.title = table.find('span', style='font-size:12pt; font-weight:bold').text.strip()
            event.time = table.find('td', style='vertical-align:top;text-align:right;min-width:200px').find('strong', recursive=False).text.strip()

            defined_matches_div = table.find('div', style='text-align:center')
            
            if defined_matches_div is None:
                continue
            
            links = defined_matches_div.find_all('a')
            
            for (o1, m, o2) in zip(*[iter(links)] * 3):
                
                opponent1 = entities.opponent.Opponent()
                opponent2 = entities.opponent.Opponent()
                
                opponent1.name = o1.text.strip()
                opponent2.name = o2.text.strip()
                
                match = entities.match.Match()
                
                match.opponent1 = opponent1
                match.opponent2 = opponent2

                match.map = m.text.strip()
                
                event.matches.append(match)
            
            events.append(event)
        
        return events
