# -*- coding: utf-8 -*-
"""Create an application instance."""
from flask.helpers import get_debug_flag

from mmr_website.app import create_app
from mmr_website.settings import Config

app = create_app(Config)
