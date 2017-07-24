from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import CSRFProtect
from flask_mail import Mail
from flask_login import LoginManager
from config import DevelopmentConfig

app = Flask(__name__)
app.config.from_object(DevelopmentConfig)

csrf = CSRFProtect(app)
mail = Mail(app)
db = SQLAlchemy(app)
lm = LoginManager(app)

# NECESSÁRIO IMPORTAR AS TABELAS ANTES DO create_all
from mainapp.models import tables
with app.app_context():
    db.create_all()

from mainapp.controllers import ssh, views, forms
