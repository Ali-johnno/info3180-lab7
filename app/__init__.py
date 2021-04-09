from flask import Flask
from flask_cors import CORS
from app.config import Config
from flask_wtf.csrf import CSRFProtect

app = Flask(__name__)

app.config.from_object(Config)
CORS(app)
csrf = CSRFProtect(app)
from app import views
