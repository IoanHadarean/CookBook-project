import os
import pymysql
from flask.logging import create_logger
from flask import Flask, redirect, render_template, request, url_for, flash, session, logging
from bson.objectid import ObjectId
from wtforms import Form, StringField, TextAreaField, PasswordField, validators
from passlib.hash import sha256_crypt


app = Flask(__name__)
LOG = create_logger(app)

#Get Username from Cloud9 Workspace
username = os.getenv('C9_USER')

#Connect to the database
connection = pymysql.connect(host = 'localhost',
                            user = username,
                            password = '',
                            db = 'flaskapp',
                            cursorclass = pymysql.cursors.DictCursor)

app.secret_key = os.getenv("SECRET", "1403goagl")

    
""" RegisterForm class with fields and validators """

class RegisterForm(Form):
    name = StringField('Name', [validators.Length(min=1, max=50)])
    username = StringField('Username', [validators.Length(min=4, max=25)])
    email = StringField('Email', [validators.Length(min=6, max=50)])
    password = PasswordField('Password', [
        validators.DataRequired(),
        validators.EqualTo('confirm', message='Passwords do not match')
        ])
    confirm = PasswordField('Confirm Password')
    
    
""" Route for new user registering to the website """

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
        
        # Save and close the connection
        connection.commit()
        cur.close()
        
            
        flash("You can now login to the website", "success")
        
        redirect(url_for('register'))
    return render_template('register.html', form=form)
    
""" Login for user already registered to the website """

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Get Form Fields
        username = request.form['username']
        password_candidate = request.form['password']
        
        # Create cursor
        cur = connection.cursor()
        
        # Get user by username
        result = cur.execute("SELECT * FROM users WHERE username = %s", [username])
        
        if result > 0:
            # Get stored hash
            data = cur.fetchone()
            password = data['password']
            
            #Compare passwords
            if sha256_crypt.verify(password_candidate, password):
                session['logged in'] = True
                session['username'] = username
                
                flash('You are now logged in', 'success')
                return redirect(url_for('dashboard'))
            else:
                error = 'Invalid login'
                return render_template('login.html', error=error)
            # Close connection
            cur.close()
        else:
            error = 'Username not found'
            return render_template('login.html', error=error)
            
    return render_template('login.html')
    
""" Logout """
@app.route('/logout')
def logout():
    session.clear()
    flash('You are now logged out', 'success')
    return redirect(url_for('login'))
    
""" User dashboard """

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')
  
  
""" Main function for running the app """      

if __name__ == "__main__":
    app.run(host=os.environ.get('IP'),
        port=int(os.environ.get('PORT')),
        debug=True)
        