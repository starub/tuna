import json
import jsonpickle
import unittest

from core.gg_scraper import GGScraper
from db.scrapes_storage import ScrapesStorage


class ScrapeStorageTest(unittest.TestCase):
    
    def test_save_scrape(self):
        
        scraper = GGScraper("counterstrike")

        storage = ScrapesStorage()
        
        raw = scraper.scrape()
        encoded = jsonpickle.encode(raw, unpicklable=False)
        json_data = json.loads(encoded)
        
        storage.add(json_data)
        
