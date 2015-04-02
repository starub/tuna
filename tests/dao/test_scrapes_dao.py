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

import json
import unittest

import jsonpickle

import dao.scrapes_dao as dao
import scrapers.gg_scraper


class ScrapesDAOTest(unittest.TestCase):
    def test_save_scrape(self):
        scraper = scrapers.gg_scraper.GGScraper("counterstrike")

        storage = dao.ScrapesDAO()

        raw = scraper.scrape()
        encoded = jsonpickle.encode(raw, unpicklable=False)
        json_data = json.loads(encoded)

        storage.add(json_data)
        
