import pymongo


class ScrapesStorage():
    
    def __init__(self):
        client = pymongo.MongoClient()
        self.db = client.tuna
        self.collection = self.db.scrapes
                
    def add(self, scrape):
        self.collection.insert(scrape)
    