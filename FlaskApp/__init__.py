import os
import logging.config

APP_SETTINGS = os.environ.get('APP_SETTINGS', 'config.DevelopmentConfig')
DEV_SERVER_NAME = os.environ.get('DEV_SERVER_NAME', 'localhost:5000')
LOGGER = os.environ.get('APP_LOGGER', 'dev')

# JSON Encoder

# BaseConverter

# logging

logging.config.fileConfig('logging.conf')
logger = logging.getLogger(LOGGER)
