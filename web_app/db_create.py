# this allows us to run a command in the heroku cli that will create our db
# go to heroku cli
# type in python db_create.py
# fin

from web_app import db

db.create_all()