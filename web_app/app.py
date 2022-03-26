import os
from flask import Flask
from dotenv import load_dotenv
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from web_app.routes import sats
from web_app.models import db, migrate, User
from flask_sqlalchemy import SQLAlchemy

import os
import re

load_dotenv()

#DATABASE_URL = os.getenv("DATABASE_URL", default="OOPS")
DATABASE_URL = os.environ.get('DATABASE_URL').replace("://", "ql://", 1)

# heroku cleanup
#SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL').replace("://", "ql://", 1)

def create_app():
    # initializing new flask app
    app = Flask(__name__)
    # just an example
    #app.config["CUSTOM_VAR"] = 5
    app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_URL
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    #SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL').replace("://", "ql://", 1)
    
    db.init_app(app)
    migrate.init_app(app, db)
    
    # linking to routes.py page via the "routes" variable
    app.register_blueprint(sats)
    
    return app
    