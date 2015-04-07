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

import unittest

import scrapers.tl_scraper as sc


class TLScraperTest(unittest.TestCase):
    
    def test_scrape(self):
        scraper = sc.TLScraper()
        events = scraper.scrape()
        for event in events:
            print(event.title)
            print(event.time)
            for match in event.matches:
                print(match.map)
                print(match.opponent1.name)
                print(match.opponent2.name)