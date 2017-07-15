from flask import Flask
from flask_wtf import CSRFProtect
from config import DevelopmentConfig

app = Flask(__name__)
app.config.from_object(DevelopmentConfig)

csrf = CSRFProtect(app)


from mainapp.controllers import ssh, views
