# -*- coding: utf-8 -*-
"""Create an application instance."""
from flask.helpers import get_debug_flag

from mrr_website.app import create_app
from mrr_website.settings import Config

app = create_app(Config)
