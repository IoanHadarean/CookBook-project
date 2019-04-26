import os, pymysql, requests, pygal, re, env
from base64 import b64encode
from PIL import Image
from os import urandom
from datetime import datetime, timedelta
from flask.logging import create_logger
from flask_login import current_user, LoginManager, login_required, login_user, logout_user
from werkzeug.datastructures import CombinedMultiDict
from flask_wtf.file import FileField, FileRequired, FileAllowed
from zapp import values
from zapp.helpers import get_results
from zapp.values import French_values, Mexican_values, Greek_values, English_values, Asian_values, Indian_values, Irish_values, Italian_values
from flask_pymongo import PyMongo, pymongo
from flask import Flask, redirect, render_template, render_template_string, request, url_for, flash, session, logging, json, jsonify
from bson.json_util import dumps
from bson.objectid import ObjectId
from flask_moment import Moment
from wtforms import Form, StringField, TextAreaField, PasswordField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from passlib.hash import sha256_crypt
from functools import wraps
from werkzeug.urls import url_parse


app = Flask(__name__)
LOG = create_logger(app)
moment = Moment(app)

# Define Flask-login configuration 

login_mgr = LoginManager(app)
login_mgr.login_view = 'login'
login_mgr.refresh_view = 'login'
login_mgr.needs_refresh_message = (u"To protect your account, please reauthenticate to access this page.")
login_mgr.needs_refresh_message_category = "info"



#Connect to MySQL database
connection = pymysql.connect(host = os.getenv("DB_HOST"),
                            user = os.getenv("DB_USERNAME"),
                            password = os.getenv("DB_PASS"),
                            db = os.getenv("DB_NAME"),
                            cursorclass = pymysql.cursors.DictCursor)

app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")

#Connect to MongoDB database

app.config["MONGO_DBNAME"] = os.getenv("MONGO_DBNAME")
app.config["MONGO_URI"] = os.getenv("MONGO_URI")

mongo = PyMongo(app)

# Get MongoDB collections

recipe_collection = mongo.db.recipes
ratings_collection = mongo.db.ratings
user_recipes = mongo.db.user_recipes

    
""" RegisterForm class with fields and validators """

class RegisterForm(Form):
    name = StringField('Name', validators = [DataRequired(), Length(min=6, max=50)])
    username = StringField('Username', validators = [DataRequired(), Length(min=6, max=25)])
    email = StringField('Email', validators = [DataRequired(), Email(), Length(min=15, max=50)])
    password = PasswordField('Password', validators = [DataRequired()])
    confirm = PasswordField('Confirm Password', validators = [DataRequired(), EqualTo('password',
                message = 'Passwords do not match')])
                

""" Edit Profile Form class with fields and validators """

class EditForm(Form):
    name = StringField('Name', validators=[DataRequired(), Length(min=6, max=50)])
    email = StringField('Email', validators = [DataRequired(), Email(), Length(min=11, max=50)])
    about_me = TextAreaField('About Me', validators=[Length(min=12, max=140)])
    picture = FileField('Update Profile Picture', validators = [FileRequired(), FileAllowed(['jpg', 'jpeg', 'png'])])
                
           
""" Log out the user from session after 1 hour """           
            
@app.before_request
def before_request():
    session.permanent = True
    app.permanent_session_lifetime = timedelta(minutes=60)
            
            
            
""" Route when first accessing the page """

@app.route('/')
def index():
    return redirect(url_for('recipes', limit=6, offset=0))
    
    
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
        
        get_db_username = cur.execute("SELECT username FROM users WHERE username = %s", form.username.data)
        get_db_email = cur.execute("SELECT email FROM users WHERE email = %s", form.email.data)
        
        if get_db_username > 0:
            flash("That username is already taken. Please choose a different one.")
        elif get_db_email > 0:
            flash("That email is already taken. Please choose a different one.")
        else:
            cur.execute("INSERT INTO users(name, email, username, password) VALUES(%s, %s, %s, %s)", (name, email, username, password))
            # Save the connection
            connection.commit()
            session['logged_in'] = True
            session['username'] = username
            flash('You are now logged in', 'success')
            return redirect(url_for('profile'))
            
            
        #Close the connection
        cur.close()
        
    return render_template('register.html', form=form)
    
    
    
    
    
""" Login for user already registered to the website """

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Get Form Fields
        username = request.form.get('username')
        password_candidate = request.form['password']
        
        # Create cursor
        cur = connection.cursor()
        
        # Get user by username
        result = cur.execute("SELECT * FROM users WHERE username = %s", username)
        
        if result > 0:
            # Get stored hash
            data = cur.fetchone()
            password = data['password']
            
            #Compare passwords
            if sha256_crypt.verify(password_candidate, password):
                session['logged_in'] = True
                session['username'] = username
                
                next_page = request.args.get('next')
                if not next_page or url_parse(next_page).netloc != '':
                    flash('You are now logged in', 'success')
                    next_page = url_for('profile')
                return redirect(next_page)
            else:
                error = 'Invalid login'
                return render_template('login.html', error=error)
            # Close connection
            cur.close()
        else:
            error = 'Username not found'
            return render_template('login.html', error=error)
            
    return render_template('login.html')
    
    
    
    
    
    
@app.route('/profile', methods = ['GET', 'POST'])
def profile():
    form = EditForm(CombinedMultiDict((request.files,request.form)))
    
    #Create cursor
    cur = connection.cursor() 
    
    #Get session username
    user = session.get('username')
    date = datetime.utcnow()
    
    #Get current username and email from db
    cur.execute("SELECT name FROM users  WHERE username = %s", user)
    current_name = cur.fetchall()[0]['name']
    cur.execute("SELECT email FROM users  WHERE username = %s", user)
    current_email = cur.fetchall()[0]['email']
    cur.execute("SELECT aboutme FROM users  WHERE username = %s", user)
    profile_description = cur.fetchall()[0]['aboutme']
    cur.execute("SELECT image FROM users  WHERE username = %s", user)
    image_file = cur.fetchall()[0]['image']
    connection.commit()
    cur.close()
    
    if request.method == 'POST' and form.validate():
        name = form.name.data
        email = form.email.data
        about_me = form.about_me.data
        picture = form.picture.data
        random_hex = urandom(16)
        token = b64encode(random_hex).decode('utf-8')
        _, f_ext = os.path.splitext(picture.filename)
        picture_fn = token + f_ext
        new_picture_fn = picture_fn.replace("/", "|")
        app.root_path = os.path.dirname(os.path.abspath(__file__))
        picture_path = os.path.abspath(os.path.join(app.root_path, 'static/images', new_picture_fn))
        
        output_size = (180, 180)
        
        i = Image.open(picture)
        i.thumbnail(output_size)
        
        i.save(picture_path)
        picture_file = new_picture_fn

        
        #Get session username
        user = session.get('username')
        
        #Create cursor
        cur = connection.cursor() 
    
        #Get current username and email from db
        cur.execute("SELECT name FROM users  WHERE username = %s", user)
        current_name = cur.fetchall()[0]['name']
        cur.execute("SELECT email FROM users  WHERE username = %s", user)
        current_email = cur.fetchall()[0]['email']
        
        
        #Check the name and email that come from the form to make sure everything is updated correctly
        
        get_db_name = cur.execute("SELECT name FROM users WHERE name = %s", name)
        get_db_email = cur.execute("SELECT email FROM users WHERE email = %s", email)
        
         
        if name != current_name:
            if get_db_name > 0:
                flash("That name is already taken. Please choose a different one.", 'danger')
            elif (get_db_email > 0 and email != current_email):
                flash("That email is already taken. Please choose a different one.", 'danger')
            else:
                cur.execute("UPDATE users SET name = %s WHERE username = %s", (name, user))
                cur.execute("UPDATE users SET email = %s WHERE username = %s", (email, user))
                cur.execute("UPDATE users SET aboutme = %s WHERE username = %s", (about_me, user))
                cur.execute("UPDATE users SET image = %s WHERE username = %s", (picture_file, user))
                flash('Your profile has been updated successfully', 'success')
                return redirect(url_for('profile'))
        elif email != current_email:
            if get_db_email > 0:
                flash("That email is already taken. Please choose a different one.", 'danger')
            elif (get_db_name > 0 and form.name.data != current_name):
                flash("That name is already taken. Please choose a different one.", 'danger')
            else:
                cur.execute("UPDATE users SET name = %s WHERE username = %s", (name, user))
                cur.execute("UPDATE users SET email = %s WHERE username = %s", (email, user))
                cur.execute("UPDATE users SET aboutme = %s WHERE username = %s", (about_me, user))
                cur.execute("UPDATE users SET image = %s WHERE username = %s", (picture_file, user))
                flash('Your profile has been updated successfully', 'success')
                return redirect(url_for('profile'))
        else:
            flash('Your profile has been updated successfully', 'success')
            cur.execute("UPDATE users SET aboutme = %s WHERE username = %s", (about_me, user))
            cur.execute("UPDATE users SET image = %s WHERE username = %s", (picture_file, user))
            return redirect(url_for('profile'))

        #Commit and close the connection
        connection.commit()
        cur.close()
    
    # Implement pagination for user recipes
        
    pagination_offset = int(request.args.get('offset', '0'))
    pagination_limit = int(request.args.get('limit', '6'))


    userMade = user_recipes.find({"username" : user})
    if userMade.count() > 0:
        starting_id = userMade.sort('_id', pymongo.ASCENDING)
        last_id = starting_id[pagination_offset]['_id']
        total_results = 0
        for recipe in userMade:
            total_results += 1
    
        args = {
            "limit": pagination_limit,
            "offset": pagination_offset,
            "recipes_sorted": user_recipes.find({"$and" : [{"username" : user}, {'_id': {'$gte' : last_id}}]}).sort('_id', pymongo.ASCENDING).limit(pagination_limit),
            "next_url": '/profile?limit=' + str(pagination_limit) + '&offset=' + str(pagination_offset + pagination_limit),
            "prev_url": '/profile?limit=' + str(pagination_limit) + '&offset=' + str(pagination_offset - pagination_limit),
            "recipes": userMade,
            "total_results": total_results
        }
        
        return render_template('profile.html', args = args, userMade = userMade, current_name = current_name, image_file = image_file, 
                            date = date, current_email = current_email, profile_description = profile_description, form=form)
    else:
         return render_template('profile.html', current_name = current_name, image_file = image_file, 
                            date = date, current_email = current_email, profile_description = profile_description, form=form)
    
    
    
""" Logout """
@app.route('/logout')
def logout():
    session.clear()
    flash('You are now logged out', 'success')
    return redirect(url_for('login'))
    
    
    
    
""" Get all recipes and implement pagination """

@app.route('/recipes', methods = ['GET', 'POST'])
def recipes():
    
    pagination_offset = int(request.args.get('offset', '0'))
    pagination_limit = int(request.args.get('limit', '6'))

    recipes = recipe_collection.find()
    starting_id = recipe_collection.find().sort('_id', pymongo.ASCENDING)
    last_id = starting_id[pagination_offset]['_id']
    total_results = 0
    for item in recipes:
        total_results +=1
    
    args = {
        "limit": pagination_limit,
        "offset": pagination_offset,
        "recipes_sorted": recipe_collection.find({'_id': {'$gte' : last_id}}).sort('_id', pymongo.ASCENDING).limit(pagination_limit),
        "next_url": '/recipes?limit=' + str(pagination_limit) + '&offset=' + str(pagination_offset + pagination_limit),
        "prev_url": '/recipes?limit=' + str(pagination_limit) + '&offset=' + str(pagination_offset - pagination_limit),
        "recipes": recipes,
        "total_results": total_results
    }
    
    cuisines = mongo.db.cuisines.find()
    courses = mongo.db.courses.find()
    allergens = mongo.db.allergens.find()
    
    return render_template('recipes.html', cuisines = cuisines, courses = courses, allergens = allergens, args=args)
  
  
  
""" Get the filter results for recipes and then 
    implement pagination for filter results """
  

@app.route('/filter_recipes', methods = ["GET", "POST"])
def filter_recipes():
    result = []
    filter_result = []
    cuisines = mongo.db.cuisines.find()
    courses = mongo.db.courses.find()
    allergens = mongo.db.allergens.find()
    if request.method == 'POST':
        form = request.form.to_dict()
        session['filter_form'] = form
        recipes = dumps(recipe_collection.aggregate([{"$match": {"$and": get_results(form)}}]))
        filter_result = json.loads(recipes)
        session['count_filter'] = str(len([x for x in filter_result]))
        count_filter = session['count_filter']
       
        #Pagination for filters when the form is submitted
        pagination_offset = int(request.args.get('offset', '0'))
        pagination_limit = int(request.args.get('limit', '6'))
    
    
        starting_id = recipe_collection.aggregate([{"$match": {"$and": get_results(form)}}, {"$sort": {"_id": 1}}])
        results_count = 0
        result = []
        for count_item in starting_id:
            results_count += 1
            result.append(count_item)
        
        if results_count != 0:
            last_id = result[pagination_offset]['_id']
        
        
            args = {
                "limit": pagination_limit,
                "offset": pagination_offset,
                "recipes_sorted": recipe_collection.aggregate([{"$match": {"$and": [{"$and": get_results(form)}, {"_id": { "$gte": last_id}}]}}, {"$sort": {"_id": 1}}, {"$limit": pagination_limit}]),
                "next_url": '/filter_recipes?limit=' + str(pagination_limit) + '&offset=' + str(pagination_offset + pagination_limit),
                "prev_url": '/filter_recipes?limit=' + str(pagination_limit) + '&offset=' + str(pagination_offset - pagination_limit),
                "total_results": results_count
            }
            
            
            return render_template('recipes.html', form = form, count_filter = count_filter,
            cuisines = cuisines, courses = courses, allergens = allergens, args = args)
        else:
            return render_template('recipes.html', form = form, count_filter = count_filter,
            cuisines = cuisines, courses = courses, allergens = allergens)
    
    
    #Pagination on GET request for filters
    pagination_offset = int(request.args.get('offset', '0'))
    pagination_limit = int(request.args.get('limit', '6'))
    form = session.get('filter_form')
    
    starting_id = recipe_collection.aggregate([{"$match": {"$and": get_results(form)}}, {"$sort": {"_id": 1}}])
    results_count = 0
    result = []
    for count_item in starting_id:
        results_count += 1
        result.append(count_item)
        
    if results_count != 0:
        last_id = result[pagination_offset]['_id']
        
        
        args = {
            "limit": pagination_limit,
            "offset": pagination_offset,
            "recipes_sorted": recipe_collection.aggregate([{"$match": {"$and": [{"$and": get_results(form)}, {"_id": { "$gte": last_id}}]}}, {"$sort": {"_id": 1}}, {"$limit": pagination_limit}]),
            "next_url": '/filter_recipes?limit=' + str(pagination_limit) + '&offset=' + str(pagination_offset + pagination_limit),
            "prev_url": '/filter_recipes?limit=' + str(pagination_limit) + '&offset=' + str(pagination_offset - pagination_limit),
            "total_results": results_count
        }
    
        return render_template('recipes.html', form = form, cuisines = cuisines, courses = courses, allergens = allergens, args = args)
    else:
        return render_template('recipes.html')


  
  
  
""" Get the search results for recipes and then 
    implement pagination for search results """
 
  

@app.route('/search_recipes', methods = ['GET', 'POST'])
def search_recipes():
    
    result = []
    parsed_result = []
    if request.method == 'POST':
        
        # Get the results from the form according to user input
        search_text = request.form.get('search_input')
        session['search_text'] = search_text
        recipe_collection.create_index([('$**', 'text')])
        result = dumps(recipe_collection.find({ "$text": { "$search": str(search_text) }}))
        parsed_result = json.loads(result)

        session['count_recipes'] = str(len([x for x in parsed_result]))
        count_recipes = session['count_recipes']
        
        
        
        #Pagination for search when the form is submitted
        pagination_offset = int(request.args.get('offset', '0'))
        pagination_limit = int(request.args.get('limit', '6'))
    
    
        recipes = recipe_collection.find({ "$text": { "$search": str(search_text) }})
        starting_id = recipe_collection.find({ "$text": { "$search": str(search_text) }}).sort('_id', pymongo.ASCENDING)
        results_count = starting_id.count()
        
        if results_count != 0 and search_text != None:
            last_id = starting_id[pagination_offset]['_id']
            total_results = 0
            for item in recipes:
                total_results +=1
        
        
            args = {
                "limit": pagination_limit,
                "offset": pagination_offset,
                "recipes_sorted": recipe_collection.find({"$and": [{ "$text": { "$search": str(search_text) }}, {'_id': {'$gte' : last_id}}]}).sort('_id', pymongo.ASCENDING).limit(pagination_limit),
                "next_url": '/search_recipes?limit=' + str(pagination_limit) + '&offset=' + str(pagination_offset + pagination_limit),
                "prev_url": '/search_recipes?limit=' + str(pagination_limit) + '&offset=' + str(pagination_offset - pagination_limit),
                "total_results": total_results
            }
        
            return render_template('search_recipes.html',
            search_text = search_text, count_recipes = count_recipes, parsed_result = parsed_result, args = args)
        else:
            return render_template('search_recipes.html',
            search_text = search_text, count_recipes = count_recipes)
            
    #Pagination for search on GET request
    pagination_offset = int(request.args.get('offset', '0'))
    pagination_limit = int(request.args.get('limit', '6'))
    search_text = session.get('search_text')
    
    recipes = recipe_collection.find({ "$text": { "$search": str(search_text) }})
    starting_id = recipe_collection.find({ "$text": { "$search": str(search_text) }}).sort('_id', pymongo.ASCENDING)
    results_count = starting_id.count()
    
    if results_count != 0 and search_text != None:
        last_id = starting_id[pagination_offset]['_id']
        total_results = 0
        for item in recipes:
            total_results +=1
        
        
        args = {
            "limit": pagination_limit,
            "offset": pagination_offset,
            "recipes_sorted": recipe_collection.find({"$and": [{ "$text": { "$search": str(search_text) }}, {'_id': {'$gte' : last_id}}]}).sort('_id', pymongo.ASCENDING).limit(pagination_limit),
            "next_url": '/search_recipes?limit=' + str(pagination_limit) + '&offset=' + str(pagination_offset + pagination_limit),
            "prev_url": '/search_recipes?limit=' + str(pagination_limit) + '&offset=' + str(pagination_offset - pagination_limit),
            "total_results": total_results
        }
        
        return render_template('search_recipes.html', args = args)
    else:
        return render_template('search_recipes.html')
   
   
""" Allow logged in user to add recipe """
@app.route('/add_recipe', methods = ['GET', 'POST'])
def add_recipe():
    cuisines = mongo.db.cuisines.find()
    courses = mongo.db.courses.find()
    allergens = mongo.db.allergens.find()
    user_recipes = mongo.db.user_recipes.find()
    return render_template('add_recipe.html', user_recipes = user_recipes, courses = courses,
                            cuisines = cuisines, allergens = allergens)   
   
   
   
   
""" Insert a recipe in the user_recipe collection """   
   
@app.route("/insert_recipe", methods=["POST"])
def insert_recipe():
    if request.method == 'POST':
        form = request.form.to_dict()
        instructions = []
        ingredients = []
        
        # Loop through the keys in the form
        # If the key matches instruction append instruction to instructions list
        for key in form:
            regex = re.compile("^instruction")
            if regex.match(key):
                instructions.append(form[key])
        
        # Loop through the keys in the form
        # If the key matches ingredient append ingredients to ingredients list
        for key in form:
            regex = re.compile("^ingredient")
            if regex.match(key):
                ingredients.append(form[key])
        
        user_recipes.insert_one({
            "ingredients": ingredients,
            "instructions": instructions,
            "allergen_name": request.form.get("allergen_name"),
            "cuisine_name": request.form.get("cuisine_name"),
            "course_name" : request.form.get("course_name"),
            "recipe_name" : request.form.get("recipe_name"),
            "recipe_image" : "https://media.self.com/photos/58f7d022feead55f43f7fc78/4:3/w_728,c_limit/Creamy-Sun-Dried-Parmesan-Chicken-cafedelites-1%25202.jpg",
            "username" : session.get("username")
        })
        
    flash ("Your recipe has been added successfully. Please note that you can not like/rate your own recipes.", "success")
    return redirect(url_for('profile'))      


""" Edit user recipe """
@app.route("/edit_recipe/<recipe_id>")
def edit_recipe(recipe_id):
    the_recipe = user_recipes.find_one({"_id": ObjectId(recipe_id)})
    cuisines = mongo.db.cuisines.find()
    courses = mongo.db.courses.find()
    allergens = mongo.db.allergens.find()
    return render_template("edit_recipe.html", the_recipe = the_recipe, cuisines = cuisines,
                            allergens = allergens, courses = courses)



""" Update user recipe """
@app.route("/update_recipe/<recipe_id>", methods=["POST"])
def update_recipe(recipe_id):
    form = request.form.to_dict()
    instructions = []
    ingredients = []
        
    # Loop through the keys in the form
    # If the key matches instruction append instruction to instructions list
    for key in form:
        regex = re.compile("^instruction")
        if regex.match(key):
            instructions.append(form[key])
        
    # Loop through the keys in the form
    # If the key matches ingredient append ingredients to ingredients list
    for key in form:
        regex = re.compile("^ingredient")
        if regex.match(key):
            ingredients.append(form[key])
    user_recipes.update({'_id': ObjectId(recipe_id)},
    {
        'username': session.get("username"),
        'recipe_image': "https://media.self.com/photos/58f7d022feead55f43f7fc78/4:3/w_728,c_limit/Creamy-Sun-Dried-Parmesan-Chicken-cafedelites-1%25202.jpg",
        'recipe_name': request.form.get('recipe_name'),
        'allergen_name': request.form.get('allergen_name'),
        'cuisine_name': request.form.get('cuisine_name'),
        'course_name': request.form.get('course_name'),
        'instructions': instructions,
        'ingredients': ingredients
    })
    flash ("Your recipe has been updated successfully", "success")
    return redirect(url_for('profile'))



""" Delete user recipe """

@app.route('/delete_recipe/<recipe_id>')
def delete_recipe(recipe_id):
    user_recipes.remove({'_id': ObjectId(recipe_id)})
    flash ('Your recipe has been deleted successfully', 'success')
    return redirect(url_for('profile'))



        
""" View details of a user recipe """

@app.route('/get_user_recipe/<recipe_id>', methods = ['GET', 'POST'])
def get_user_recipe(recipe_id):
    user_recipe = user_recipes.find_one({"_id": ObjectId(recipe_id)})
    return render_template("get_user_recipe.html", user_recipe = user_recipe)
    
    



""" View details of a database recipe """

@app.route('/get_recipe/<recipe_id>', methods = ['GET', 'POST'])
def get_recipe(recipe_id):
    
    the_recipe = recipe_collection.find_one({"_id": ObjectId(recipe_id)})
    
    """ Add ready time for each recipe (cooking time + preparation time) """
    
    cooking_time = the_recipe["cooking_time"].split(" ")
    preparation_time = the_recipe["preparation_time"].split(" ")
    minutes_total = 0
    final_minutes = 0
    final_hours = 0
    ready_time_cooking = 0
    ready_time_preparation = 0
    if "h" not in cooking_time[0]:
        minutes_cooking_time = int(cooking_time[0])
        ready_time_cooking += minutes_cooking_time
    else:
        hours_cooking_time = int(cooking_time[0][0])
        minutes_cooking_time = int(cooking_time[1])
        hours_to_minutes = hours_cooking_time * 60
        ready_time_cooking = hours_to_minutes + minutes_cooking_time
    if "h" not in preparation_time[0]:
        minutes_preparation_time = int(preparation_time[0])
        ready_time_preparation += minutes_preparation_time
    else:
        hours_preparation_time = preparation_time[0][0]
        minutes_preparation_time = preparation_time[1]
        hours_to_minutes = hours_preparation_time * 60
        ready_time_preparation = hours_to_minutes + minutes_preparation_time
    minutes_total = ready_time_cooking + ready_time_preparation
    final_hours = minutes_total // 60
    final_minutes = minutes_total % 60
    if final_hours == 0:
        total = "%s min" % final_minutes
    elif final_minutes == 0:
        total = "%sh" % final_hours
    else:
        total = "%sh %s min" % (final_hours, final_minutes)
        
        
    """ Added quantities for each recipe using regex """
    
    ingredients = the_recipe["ingredients"]
    full_quantities = []
    full_ingredients = []
    for ingredient in ingredients:
        concatenated_quantity = ''
        concatenated_ingredient = ''
        ingredientSplit = ingredient.split(" ")
        i = 0
        while i < len(ingredientSplit):
            firstElement = ingredientSplit[i]
            regex = re.findall("(^(clove|cup|teaspoon|tablespoon|\d(?<!-)$|ounce|inch|pound|pinch|slices?(?<!d)$|milliliter)|.\d)", firstElement)
            if regex:
                concatenated_quantity += "{} ".format(ingredientSplit[i])
            else:
                concatenated_ingredient += "{} ".format(ingredientSplit[i])
            i += 1
        full_quantities.append(concatenated_quantity)
        full_ingredients.append(concatenated_ingredient)
        
    """ Get the rating text for each rating done by each user for each recipe
        and check for user None value """
    
    # Get MySQL connection
    cur = connection.cursor()

    user = session.get('username')
    recipe_number = the_recipe["id"]
    
    instance_rating = []
    if user != None:
        cur.execute("SELECT id FROM users WHERE username = %s", user)
        user_id = cur.fetchall()[0]['id']
        print(user_id)
    
        instance_rating = ratings_collection.find_one({"user_id": user_id, "recipe_id": recipe_number})
        if instance_rating == None:
            ratings_collection.insert_one({"user_id": user_id, "recipe_id": recipe_number, "rateText": "Rate Recipe"})

        # Close the connection
        connection.commit()
        cur.close()
    else:
        return render_template('get_recipe.html', user =  user, recipe=the_recipe, total = total, full_quantities = full_quantities,
                            full_ingredients = full_ingredients)
            
    return render_template('get_recipe.html', user =  user, recipe=the_recipe, total = total, full_quantities = full_quantities,
                            full_ingredients = full_ingredients, instance_rating = instance_rating)
    
    
    
    

""" Like recipe """

@app.route('/like/<recipe_id>', methods = ['GET', 'POST'])
def like(recipe_id):
    
    # Get MySQL connection
    cur = connection.cursor()
    
    #Get variables
    user = session['username']
    recipe = recipe_collection.find_one({"_id": ObjectId(recipe_id)})
    recipe_number = recipe["id"]
    likes = recipe["likes"]
    
    # Check if a record with the user and the recipe exists in the user likes table in the flaskapp database
    # If it does not then insert the new record into the user likes table
    # Get the liked flag and check if it's 0 or 1
    # If it's 1 then update the number of likes
    # Finally, set the liked flag to 0 so a recipe can not be liked anymore
    # Commit to the database and redirect
    cur.execute("SELECT id FROM users WHERE username = %s", user)
    user_id = cur.fetchall()[0]['id']
    cur.execute("SELECT userId, recipeId, liked, unliked FROM userlikes WHERE userId = %s AND recipeId = %s", (user_id, recipe_number))
    result = cur.fetchall()
    if len(result) == 0:
        cur.execute("INSERT INTO userlikes(userId, recipeId) VALUES(%s, %s)", (user_id, recipe_number))
    cur.execute("SELECT userId, recipeId, liked, unliked FROM userlikes WHERE userId = %s AND recipeId = %s", (user_id, recipe_number))
    likedFlag = cur.fetchall()[0]['liked']
    if (likedFlag != 0):
        likes = likes + 1
        recipe_collection.update({'_id': ObjectId(recipe_id)}, {
                                  "$set": {"likes": likes}})
        cur.execute("UPDATE userlikes SET liked = '0' WHERE userId = %s AND recipeId = %s", (user_id, recipe_number))
        cur.execute("UPDATE userlikes SET unliked = '1' WHERE userId = %s AND recipeId = %s", (user_id, recipe_number))
        
        connection.commit()
        cur.close()
        
    return json.jsonify({'likes': likes, 'recipe_id': recipe_id})
    
    
    
    
""" Dislike recipe """

@app.route('/dislike/<recipe_id>', methods = ['GET', 'POST'])
def dislike(recipe_id):
    # Get MySQL connection
    cur = connection.cursor()
    
    #Get variables
    user = session['username']
    recipe = recipe_collection.find_one({"_id": ObjectId(recipe_id)})
    recipe_number = recipe["id"]
    likes = recipe["likes"]
    
    # Check if a record with the user and the recipe exists in the user likes table in the flaskapp database
    # If it does not then insert the new record into the user likes table
    # Get the unliked flag and check if it's 0 or 1
    # If it's 1 then update the number of likes
    # Finally, set the unliked flag to 0 so a recipe can not be disliked anymore
    # Commit to the database and redirect
    cur.execute("SELECT id FROM users WHERE username = %s", user)
    user_id = cur.fetchall()[0]['id']
    cur.execute("SELECT userId, recipeId, liked, unliked FROM userlikes WHERE userId = %s AND recipeId = %s", (user_id, recipe_number))
    result = cur.fetchall()
    if len(result) == 0:
        cur.execute("INSERT INTO userlikes(userId, recipeId) VALUES(%s, %s)", (user_id, recipe_number))
    cur.execute("SELECT userId, recipeId, liked, unliked FROM userlikes WHERE userId = %s AND recipeId = %s", (user_id, recipe_number))
    unlikedFlag = cur.fetchall()[0]['unliked']
    if (unlikedFlag != 0):
        likes = likes - 1
        recipe_collection.update({'_id': ObjectId(recipe_id)}, {
                                  "$set": {"likes": likes}})
        cur.execute("UPDATE userlikes SET unliked = '0' WHERE userId = %s AND recipeId = %s", (user_id, recipe_number))
        cur.execute("UPDATE userlikes SET liked = '1' WHERE userId = %s AND recipeId = %s", (user_id, recipe_number))
        connection.commit()
        cur.close()
        
    return json.jsonify({'likes': likes, 'recipe_id': recipe_id})




    
"""  Get ratings from users and store them in the database
     then return the average rating for a recipe"""
     
@app.route('/update_rating/<recipe_id>', methods = ['GET', 'POST'])
def update_rating(recipe_id):
    if request.method == 'POST':
        # Get MySQL connection
        cur = connection.cursor()
        
        # Get variables
        rating = request.form.get('rating')
        user = session['username']
        recipe = recipe_collection.find_one({"_id": ObjectId(recipe_id)})
        recipe_number = recipe["id"]
        formatted_average = 0
        numbers_array = [1, 2, 3, 4, 5]
        
        cur.execute("SELECT id FROM users WHERE username = %s", user)
        user_id = cur.fetchall()[0]['id']
        
        instance_record = ratings_collection.find_one({"user_id": user_id, "recipe_id": recipe_number})
        if instance_record != None:
            ratings_collection.update({"user_id": user_id, "recipe_id": recipe_number},
                                    { "$set": { "rating": rating }})
            ratings_collection.update({"user_id": user_id, "recipe_id": recipe_number},
                                    { "$set": { "rateText": "Edit Rating" }})
        else:
            ratings_collection.insert_one({"user_id": user_id, "recipe_id": recipe_number, "rating": rating })
        
        
        instance_recipe = ratings_collection.find({"recipe_id": recipe_number })
        instance_count = ratings_collection.count_documents({"recipe_id": recipe_number })
        sum_rating = 0
        for doc in instance_recipe:
            sum_rating = sum_rating + int(doc["rating"])
        average_rating = sum_rating / instance_count
        if average_rating not in numbers_array:
            formatted_average =  "{:.1f}".format(average_rating)
        else:
            formatted_average = int(average_rating)
            
        
        recipe_collection.update({"_id": ObjectId(recipe_id)},
                                    { "$set": { "rating": formatted_average}})
                                    
        
    return redirect(url_for('get_recipe', recipe_id = recipe_id))


""" Recipe ingredients statistics by cuisine """

@app.route('/statistics')
def charts():
    """ Recipe ingredients statistics by cuisine """
    
    dot_chart = pygal.Dot(x_label_rotation=30, print_values = False, show_legend = False, style=pygal.style.styles['default'](value_font_size=30, title_font_size=30, 
                         legend_font_size=30, dots_size=3000, background = 'transparent', tooltip_font_size=30, label_font_size=22))
    dot_chart.title = 'Recipe Ingredients Statistics by Cuisine'
    dot_chart.y_title = 'Recipes by cuisine'
    dot_chart.x_labels = ['milk', 'egg', 'sugar', 'flour', 'salt', 'water', 'garlic', 'vanilla', 'butter']
    dot_chart.y_labels = ['French - 4', 'Mexican - 2', 'Greek - 2', 'English - 2', 'Asian - 4', 'Indian - 3', 'Irish - 2', 'Italian - 5']
    dot_chart.add('French', French_values)
    dot_chart.add('Mexican', Mexican_values)
    dot_chart.add('Greek', Greek_values)
    dot_chart.add('English', English_values)
    dot_chart.add('Asian', Asian_values)
    dot_chart.add('Indian', Indian_values)
    dot_chart.add('Irish', Irish_values)
    dot_chart.add('Italian', Italian_values)
    dot_chart = dot_chart.render(is_unicode=True)
    
    """ Recipe allergens statistics (in %) """
    
    solid_gauge_chart = pygal.SolidGauge(inner_radius=0.70, style=pygal.style.styles['default'](value_font_size=25, title_font_size=30,
                                        legend_font_size=30, background = 'transparent', tooltip_font_size=30))
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
                                legend_font_size=30, background = 'transparent', tooltip_font_size=30, label_font_size=25))
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

    
    
""" Handle error 404 """

@app.errorhandler(404)
def page_not_found(error):
    return render_template('error404.html'), 404
    
    
    
""" Handle database error """

@app.errorhandler(500)
def database_error(error):
    return render_template('error500.html'), 500
  
  
 
  
""" Main function for running the app """      

if __name__ == "__main__":
    app.run(host=os.environ.get('IP'),
        port=int(os.environ.get('PORT')),
        debug=True)
        