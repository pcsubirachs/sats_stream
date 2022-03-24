import os
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# to initialize this databse in TablePlus or similar
# this needs to be done so the program knows what framework/database to push data to
# otherwise, it will throw an error

# in cmd line
#1.)
# flask db init

#2.)
# flask db migrate

#3.)
# flask db upgrade

db = SQLAlchemy()
migrate = Migrate()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    ln_address = db.Column(db.String(128))
    link = db.Column(db.String(128))

