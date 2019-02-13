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
    
""" RegisterForm class with fields and validators"""

class RegisterForm(Form):
    name = StringField('Name', [validators.Length(min=1, max=50)])
    username = StringField('Username', [validators.Length(min=4, max=25)])
    email = StringField('Email', [validators.Length(min=6, max=50)])
    password = PasswordField('Password', [
        validators.DataRequired(),
        validators.EqualTo('confirm', message='Passwords do not match')
        ])
    confirm = PasswordField('Confirm Password')
    
"""Route for new user registering to the website"""

@app.route('/register', methods=['GET', 'POST'])
def register():
    #setting a variable equal to the RegisterForm class
    form = RegisterForm(request.form)
    if request.method == 'POST' and form.validate():
        return render_template('register.html')
    
    return render_template('register.html', form=form)
        

if __name__ == "__main__":
    app.run(host=os.environ.get('IP'),
        port=int(os.environ.get('PORT')),
        debug=True)