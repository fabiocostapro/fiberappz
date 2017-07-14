import os
import os.path
basedir = os.path.abspath(os.path.dirname("__file__"))


class Config(object):
    SECRET_KEY = os.environ.get("FLASK_SECRET_KEY")
    MAIL_SERVER = "smtp.gmail.com"
    MAIL_PORT = 587
    MAIL_USE_SSL = False
    MAIL_USE_TLS = True
    MAIL_USERNAME = "fiberappz@gmail.com"
    MAIL_PASSWORD = os.environ.get("PASSWORD_EMAIL_FI")


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(basedir, "storage.db")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
