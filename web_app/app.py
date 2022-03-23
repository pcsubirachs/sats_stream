import os
from flask import Flask
#from dotenv import load_dotenv
#from flask_sqlalchemy import SQLAlchemy
#from flask_migrate import Migrate

from web_app.routes import sats
#from web_app.models import db, migrate, User, Wallet 
#from flask_qrcode import QRcode
#from flask_sqlalchemy import SQLAlchemy


#load_dotenv()

#DATABASE_URL = os.getenv("DATABASE_URL", default="OOPS")

def create_app():
    # initializing new flask app
    app = Flask(__name__)
    # just an example
    #app.config["CUSTOM_VAR"] = 5
    #app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_URL
    #app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    
    # linking to routes.py page via the "routes" variable
    app.register_blueprint(sats)
    
    return app