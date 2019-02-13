import os
import pymysql
from flask import Flask, redirect, render_template, request, url_for, flash, session, logging
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from wtforms import Form, StringField, TextAreaField, PasswordField, validators
from passlib.hash import sha256_crypt


app = Flask(__name__)


#Get Username from Cloud9 Workspace
username = os.getenv('C9_USER')

#Connect to the database
connection = pymysql.connect(host = 'localhost',
                            user = username,
                            password = '',
                            db = 'flaskapp',
                            cursorclass = pymysql.cursors.DictCursor)

app.secret_key = os.getenv("SECRET", "1403goagl")
    
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

@app.route('/', methods=['GET', 'POST'])
def register():
    #setting a variable equal to the RegisterForm class
    form = RegisterForm(request.form)
    if request.method == 'POST' and form.validate():
        name = form.name.data
        email = form.email.data
        username = form.username.data
        password = sha256_crypt.encrypt(str(form.password.data))
        
        #Create cursor
        cur = connection.cursor()
        cur.execute("INSERT INTO users(name, email, username, password) VALUES(%s, %s, %s, %s)", (name, email, username, password))
        
        connection.commit()
        cur.close()
        
            
        flash("You can now login to the website", "success")
        
        redirect(url_for('register'))
    return render_template('register.html', form=form)
        

if __name__ == "__main__":
    app.run(host=os.environ.get('IP'),
        port=int(os.environ.get('PORT')),
        debug=True)