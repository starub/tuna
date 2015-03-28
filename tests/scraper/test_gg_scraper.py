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

from scrapers.gg_scraper import GGScraper


class GGScraperTest(unittest.TestCase):
    def test_scrape_all(self):
        scrapers = [GGScraper('counterstrike'), GGScraper('dota2'), GGScraper('lol'), GGScraper('hearthstone'),
                    GGScraper('heroesofthestorm')]

        with ThreadPoolExecutor(max_workers=len(scrapers)) as executor:
            results = list(executor.map(lambda scraper: scraper.scrape(), scrapers))

        print(jsonpickle.encode(results, unpicklable=False))


    @unittest.skip
    def test_csgo(self):
        scraper = GGScraper('counterstrike')

        matches = scraper.scrape()

        print(jsonpickle.encode(matches['live'], unpicklable=False))
        print(jsonpickle.encode(matches['upcoming'], unpicklable=False))

    @unittest.skip
    def test_dota2(self):
        scraper = GGScraper('dota2')

        matches = scraper.scrape()

        print(jsonpickle.encode(matches['live'], unpicklable=False))
        print(jsonpickle.encode(matches['upcoming'], unpicklable=False))

    @unittest.skip
    def test_lol(self):
        scraper = GGScraper('lol')

        matches = scraper.scrape()

        print(jsonpickle.encode(matches['live'], unpicklable=False))
        print(jsonpickle.encode(matches['upcoming'], unpicklable=False))

    @unittest.skip
    def test_hearthstone(self):
        scraper = GGScraper('hearthstone')

        matches = scraper.scrape()

        print(jsonpickle.encode(matches['live'], unpicklable=False))
        print(jsonpickle.encode(matches['upcoming'], unpicklable=False))

    @unittest.skip
    def test_hots(self):
        scraper = GGScraper('heroesofthestorm')

        matches = scraper.scrape()

        print(jsonpickle.encode(matches['live'], unpicklable=False))
        print(jsonpickle.encode(matches['upcoming'], unpicklable=False))
