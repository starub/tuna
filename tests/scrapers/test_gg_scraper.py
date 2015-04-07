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

from concurrent.futures.thread import ThreadPoolExecutor
import unittest

import jsonpickle

import scrapers.gg_scraper as sc


class GGScraperTest(unittest.TestCase):

    def test_scrape_all(self):
        scrapers = [sc.GGScraper('counterstrike'), sc.GGScraper('dota2'), sc.GGScraper('lol'), sc.GGScraper('hearthstone'),
                    sc.GGScraper('heroesofthestorm')]

        with ThreadPoolExecutor(max_workers=len(scrapers)) as executor:
            results = list(executor.map(lambda scraper: scraper.scrape(), scrapers))

        print(jsonpickle.encode(results, unpicklable=False))

    def test_csgo(self):
        scraper = sc.GGScraper('counterstrike')

        events = scraper.scrape()

        print(jsonpickle.encode(events['live'], unpicklable=False))
        print(jsonpickle.encode(events['upcoming'], unpicklable=False))

    def test_dota2(self):
        scraper = sc.GGScraper('dota2')

        events = scraper.scrape()

        print(jsonpickle.encode(events['live'], unpicklable=False))
        print(jsonpickle.encode(events['upcoming'], unpicklable=False))

    def test_lol(self):
        scraper = sc.GGScraper('lol')

        events = scraper.scrape()

        print(jsonpickle.encode(events['live'], unpicklable=False))
        print(jsonpickle.encode(events['upcoming'], unpicklable=False))

    def test_hearthstone(self):
        scraper = sc.GGScraper('hearthstone')

        events = scraper.scrape()

        print(jsonpickle.encode(events['live'], unpicklable=False))
        print(jsonpickle.encode(events['upcoming'], unpicklable=False))

    def test_hots(self):
        scraper = sc.GGScraper('heroesofthestorm')

        events = scraper.scrape()

        print(jsonpickle.encode(events['live'], unpicklable=False))
        print(jsonpickle.encode(events['upcoming'], unpicklable=False))
