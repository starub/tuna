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

import scrapers.base_scraper as scraper

class TLScraper(scraper.BaseScraper):
    
    def __init__(self):
        super().__init__()
   
    def scrape(self):
        
        now = datetime.date.today()

        rootUrl = 'http://www.teamliquid.net/calendar/{}/{}/?tourney=16'.format(now.year, now.strftime('%m'))

        html = super(TLScraper,self).get_html(rootUrl)
        
        today_div = html.find('div', id = 'calendar_{}content'.format(now.day)).find_all('div',style={'padding-left' : '5px'})
        
        for div in today_div:
            print(div)