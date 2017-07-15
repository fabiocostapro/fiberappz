import os


class Config(object):
    SECRET_KEY = os.environ.get("FLASK_SECRET_KEY")


class DevelopmentConfig(Config):
    DEBUG = True
