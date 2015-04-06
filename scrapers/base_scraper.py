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

import urllib
import bs4
import traceback
import fake_useragent
import config.config as cfg

class BaseScraper:

    def __init__(self):
        self.ua = fake_useragent.UserAgent()
        self.logger = cfg.get_logger(__name__)
    
    def get_html(self, url):

        headers = {'User-Agent': self.ua.random, 'Referer': url, 'Pragma': 'no-cache'}

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
