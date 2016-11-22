# -*- coding: utf-8 -*-
"""Application configuration."""
import os


class Config(object):

    secret_key = os.environ.get('MMR-WEBSITE_SECRET', 'secret-key')  # TODO: Change me
    app_dir = os.path.abspath(os.path.dirname(__file__))  # This directory
    project_root = os.path.abspath(os.path.join(app_dir, os.pardir))
    bcrypt_log_rounds = 13
    assets_debug = False
    debug_tb_enabled = False  # disable debug toolbar
    debug_tb_intercept_redirects = False
    cache_type = 'simple'  # can be "memcached", "redis", etc.
    sqlalchemy_track_modifications = False
    env = 'dev'
    debug = True
    db_name = 'dev.db'
    # put the db file in project root
    db_path = os.path.join(project_root, db_name)
    sqlalchemy_database_uri = 'sqlite:///{0}'.format(db_path)
    debug_tb_enabled = True
    assets_debug = True  # don't bundle/minify static assets
    cache_type = 'simple'  # can be "memcached", "redis", etc.
