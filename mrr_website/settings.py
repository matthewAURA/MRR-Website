# -*- coding: utf-8 -*-
"""Application configuration."""
import os


class Config(object):
    app_dir = os.path.abspath(os.path.dirname(__file__))  # This directory
    project_root = os.path.abspath(os.path.join(app_dir, os.pardir))
    env = 'dev'
    debug = True
