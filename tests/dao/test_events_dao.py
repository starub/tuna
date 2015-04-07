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
import jsonpickle
import unittest

import dao.events_dao as dao
import scrapers.gg_scraper
import scrapers.tl_scraper


class EventsDAOTest(unittest.TestCase):
    def test_save_scrape(self):

        gg_scraper = scrapers.gg_scraper.GGScraper("counterstrike")
        tl_scraper = scrapers.tl_scraper.TLScraper()

        events_dao = dao.EventsDAO()

        events_dao.add(json.loads(jsonpickle.encode(gg_scraper.scrape(), unpicklable=False)))
        events_dao.add(json.loads(jsonpickle.encode(tl_scraper.scrape(), unpicklable=False)))
        
