import os, pymysql, json, requests
import pygal
from flask.logging import create_logger
from flask_pymongo import PyMongo
from flask import Flask, redirect, render_template, request, url_for, flash, session, logging
from bson.objectid import ObjectId
from wtforms import Form, StringField, TextAreaField, PasswordField, validators
from passlib.hash import sha256_crypt
from functools import wraps


app = Flask(__name__)
LOG = create_logger(app)

#Get Username from Cloud9 Workspace
username = os.getenv('C9_USER')

#Connect to MySQL database
connection = pymysql.connect(host = 'localhost',
                            user = username,
                            password = '',
                            db = 'flaskapp',
                            cursorclass = pymysql.cursors.DictCursor)

app.secret_key = os.getenv("SECRET", "1403goagl")

#Connect to MongoDB database

app.config["MONGO_DBNAME"] = "recipes"
app.config["MONGO_URI"] = "mongodb://me:1403Goagl@ds145923.mlab.com:45923/recipes"

mongo = PyMongo(app)


    
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
    
"""Route when first accessing the page"""

@app.route('/')
def index():
    return redirect(url_for('register'))
    
""" Route for new user registering to the website """

@app.route('/register', methods=['GET', 'POST'])
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
                session['logged_in'] = True
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
    
""" Check if user is logged in """
def is_logged_in(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            flash('Unauthorized, please login', 'danger')
            return redirect(url_for('login'))
    return wrap
    
""" Logout """
@app.route('/logout')
def logout():
    session.clear()
    flash('You are now logged out', 'success')
    return redirect(url_for('login'))
    
""" User dashboard """

@app.route('/dashboard')
@is_logged_in
def dashboard():
    return render_template('dashboard.html')
    
    
""" Recipe ingredients statistics by cuisine
    (Note: all values have been multiplied by 3000
    to better reflect the statistics)"""
@app.route('/statistics')
@is_logged_in
def charts():
    """ Recipe ingredients statistics by cuisine """
    
    dot_chart = pygal.Dot(x_label_rotation=30, style=pygal.style.styles['default'](value_font_size=30, title_font_size=30, 
                         legend_font_size=30, tooltip_font_size=30, label_font_size=22))
    dot_chart.title = 'Recipe Ingredients Statistics by Cuisine'
    dot_chart.x_title = 'Ingredients'
    dot_chart.y_title = 'Recipes by cuisine'
    dot_chart.x_labels = ['milk', 'egg', 'sugar', 'flour', 'salt', 'water', 'garlic', 'vanilla', 'butter']
    dot_chart.y_labels = ['12000', '6000', '6000', '6000', '12000', '9000', '6000']
    dot_chart.add('French', [3000, 6000, 6000, 6000, 6000, 0, 0, 6000, 9000])
    dot_chart.add('Mexican', [0, 0, 0, 3000, 3000, 0, 0, 0, 0, 0])
    dot_chart.add('Greek', [0, 3000, 0, 0, 6000, 0, 6000, 0, 0])
    dot_chart.add('English', [0, 3000, 0, 3000, 6000, 3000, 0, 0, 3000])
    dot_chart.add('Asian', [0, 3000, 3000, 0, 0, 6000, 6000, 0, 3000])
    dot_chart.add('Indian', [0, 0, 6000, 0, 3000, 3000, 6000, 0, 0])
    dot_chart.add('Irish', [0, 6000, 6000, 6000, 0, 0, 0, 3000, 6000])
    dot_chart = dot_chart.render(is_unicode=True)
    
    """ Recipe allergens statistics (in %) """
    
    solid_gauge_chart = pygal.SolidGauge(inner_radius=0.70, style=pygal.style.styles['default'](value_font_size=25, title_font_size=30,
                                        legend_font_size=30, tooltip_font_size=30))
    solid_gauge_chart.title = 'Recipe Allergens Statistics (in %)'
    percent_formatter = lambda x: '{:.10g}%'.format(x)
    solid_gauge_chart.value_formatter = percent_formatter

    solid_gauge_chart.add('Egg', [{'value': 37.5, 'max_value': 100}])
    solid_gauge_chart.add('Milk', [{'value': 8.33, 'max_value': 100}])
    solid_gauge_chart.add('Nuts', [{'value': 4.16, 'max_value': 100}])
    solid_gauge_chart.add('Garlic', [{'value': 41.66, 'max_value': 100}])
    solid_gauge_chart.add('No allergens', [{'value': 25, 'max_value': 100}])
    solid_gauge_chart = solid_gauge_chart.render(is_unicode=True)
    
    """ Average calories by cuisine """
    
    gauge_chart = pygal.Gauge(human_readable=True, style=pygal.style.styles['default'](value_font_size=30, title_font_size=30, 
                                legend_font_size=30, tooltip_font_size=30, label_font_size=25))
    gauge_chart.title = 'Average calories by cuisine'
    gauge_chart.range = [0, 1000]
    gauge_chart.add('French', 393.5)
    gauge_chart.add('Mexican', 296)
    gauge_chart.add('Greek', 599)
    gauge_chart.add('English', 476)
    gauge_chart.add('Asian', 292)
    gauge_chart.add('Indian', 204.66)
    gauge_chart.add('Irish', 413.5)
    gauge_chart.add('All', 344.91)
    gauge_chart = gauge_chart.render(is_unicode=True)
    
    
    return render_template('statistics.html', dot_chart=dot_chart, solid_gauge_chart=solid_gauge_chart, gauge_chart = gauge_chart)

    
  
""" Main function for running the app """      

if __name__ == "__main__":
    app.run(host=os.environ.get('IP'),
        port=int(os.environ.get('PORT')),
        debug=True)
        