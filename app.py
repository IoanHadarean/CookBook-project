import os
from flask import Flask, redirect, render_template, request, url_for, flash, session, logging
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from flask_mysqldb import MySQL
from wtforms import Form, StringField, TextAreaField, PasswordField, validators
from passlib.hash import sha256_crypt


app = Flask(__name__)
app.secret_key = os.getenv("SECRET", "1403goagl")
app.config["MONGO_DBNAME"] = "recipes"
app.config["MONGO_URI"] = "mongodb://goagl:3markHero@ds145923.mlab.com:45923/recipes"

mongo = PyMongo(app)

@app.route('/', methods = ["GET", "POST"])
def index():
    """Main page with instructions"""
    
    if request.method == "POST":
        session["username"] = request.form["username"]
        
    if "username" in session:
        return redirect(url_for("user", username = session["username"]))
        
    return render_template("user.html")
    
@app.route('/index.html/<username>', methods = ["GET", "POST"])
def user(username):
    """Login for user"""
    
    if request.method == "POST":
        username = session["username"]
        return redirect(url_for("user", username = session["username"]))
        
    return render_template("index.html", username = username)
    
class RegisterForm(Form):
    name = StringField('Name', [validators.Length(min=1, max=50)])
    username = StringField('Username', [validators.Length(min=4, max=25)])
    email = StringField('Email', [validators.Length(min=6, max=50)])
    password = PasswordField('Password', [
        validators.DataRequired(),
        validators.EqualTo('confirm', message='Passwords do not match')
        ])
    confirm = PasswordField('Confirm Password')

if __name__ == "__main__":
    app.run(host=os.environ.get('IP'),
        port=int(os.environ.get('PORT')),
        debug=True)