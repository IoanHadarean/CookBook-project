import os
import pymysql
from flask_paranoid import Paranoid
from flask.logging import create_logger
from flask import Flask
from flask_pymongo import PyMongo, pymongo
from flask_sslify import SSLify

if not os.environ.get("DEVELOPMENT"):
    from app import env

app = Flask(__name__)
sslify = SSLify(app)
LOG = create_logger(app)


# Connect to MySQL database
connection = pymysql.connect(host=os.getenv("DB_HOST"),
                             user=os.getenv("DB_USERNAME"),
                             password=os.getenv("DB_PASS"),
                             db=os.getenv("DB_NAME"),
                             cursorclass=pymysql.cursors.DictCursor)

app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")

# Connect to MongoDB database

app.config["MONGO_DBNAME"] = os.getenv("MONGO_DBNAME")
app.config["MONGO_URI"] = os.getenv("MONGO_URI")


mongo = PyMongo(app)

""" Cookie and Session Security Implementation
Note: paranoid is necessary in terms of security for the project.
However, disable it when using Chrome Developer Tools
or a similar tool since it automatically clears the session
when accessing a different device.
"""
paranoid = Paranoid(app)
paranoid.redirect_view = '/'
SESSION_COOKIE_SECURE = True
SESSION_PERMANENT = False

from app.routes import routes