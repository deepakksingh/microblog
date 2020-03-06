from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy 
from flask_migrate import Migrate 

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)


from app import routes, models

#models: is used to define the structure of the database

#migration: most of the relational databases are centered around 
#structured data, so when the structure changes the data that
#is already in the database, the database needs to be migrated
#to the modified structure.
