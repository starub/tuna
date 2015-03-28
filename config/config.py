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

import os
import configparser
import logging

TUNA_CONFIG = configparser.ConfigParser()

TUNA_CONFIG.read(os.path.join(os.path.abspath(os.path.dirname(__file__)), 'scrapers.ini'))
TUNA_CONFIG.read(os.path.join(os.path.abspath(os.path.dirname(__file__)), 'db.ini'))
TUNA_CONFIG.read(os.path.join(os.path.abspath(os.path.dirname(__file__)), 'logging.ini'))

logging.basicConfig(format='%(asctime)s - %(levelname)s - %(name)s - %(message)s',
                    level=TUNA_CONFIG.get('LOGGING', 'level'))


def get_logger(name):
    logger = logging.getLogger(name)
    return logger