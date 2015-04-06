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

import dao.base_dao as dao

import config.config as cfg


class ScrapesDAO(dao.BaseDAO):
    def __init__(self):
        super().__init__()
        self.collection = super(ScrapesDAO, self).get_client()[cfg.TUNA_CONFIG.get('MONGODB', 'db_name')][
            cfg.TUNA_CONFIG.get('MONGODB', 'scrapes_collection')]

    def add(self, scrape):
        self.collection.insert(scrape)
    