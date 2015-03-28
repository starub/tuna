from concurrent.futures.thread import ThreadPoolExecutor
import jsonpickle
import unittest

from core.gg_scraper import GGScraper


class GGScraperTest(unittest.TestCase):

    def test_crawl_all(self):
        
        scrapers = [GGScraper('counterstrike'), GGScraper('dota2'), GGScraper('lol'), GGScraper('hearthstone'), GGScraper('heroesofthestorm')]

        with ThreadPoolExecutor(max_workers=len(scrapers)) as executor:
            results = list(executor.map(lambda crawler: crawler.scrape(), scrapers))
        
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
