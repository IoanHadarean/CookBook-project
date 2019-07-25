import pymysql
import re
import os
import requests
from app import app, connection, mongo
from flask_login import current_user, login_required, login_user, logout_user
from base64 import b64encode
from PIL import Image
from os import urandom
from datetime import datetime, timedelta
from flask_pymongo import PyMongo, pymongo
from app.models.helpers import get_results
from flask import redirect, render_template, render_template_string
from flask import request, url_for, flash, session, logging, json, jsonify
from bson.json_util import dumps
from bson.objectid import ObjectId
from passlib.hash import sha256_crypt
from functools import wraps
from werkzeug.urls import url_parse
from werkzeug.datastructures import CombinedMultiDict
from app.models.forms import RegisterForm, EditForm
from app.models.graphs import Graphs

# Get MongoDB collections

recipe_collection = mongo.db.recipes
ratings_collection = mongo.db.ratings
user_recipes = mongo.db.user_recipes

# Create index for text search
recipe_collection.create_index([('$**', 'text')])


""" Log out the user from session after 1 hour """


@app.before_request
def before_request():
    now = datetime.now()
    try:
        last_active = session['last_active']
        delta = now - last_active
        if delta.seconds > 3600 and session.get('logged_in') is True:
            session['last_active'] = now
            session.clear()
            flash('Your session has expired after 1 hour, you have been logged out', 'info')
            return redirect(url_for('login'))
    except:
        pass
    try:
        session['last_active'] = now
    except:
        pass


""" Route when first accessing the page """


@app.route('/')
def index():
    return redirect(url_for('recipes', limit=6, offset=0))


""" Route for new user registering to the website """


@app.route('/register', methods=['GET', 'POST'])
def register():
    # setting a variable equal to the RegisterForm class
    form = RegisterForm(request.form)
    if request.method == 'POST' and form.validate():
        name = form.name.data
        email = form.email.data
        username = form.username.data
        password = sha256_crypt.encrypt(str(form.password.data))

        # Create cursor
        cur = connection.cursor()

        get_db_username = cur.execute("SELECT username FROM users WHERE username = %s;", (form.username.data,))
        get_db_email = cur.execute("SELECT email FROM users WHERE email = %s;", (form.email.data,))

        if get_db_username > 0:
            flash("That username is already taken. Please choose a different one.")
        elif get_db_email > 0:
            flash("That email is already taken. Please choose a different one.")
        else:
            cur.execute("INSERT INTO users(name, email, username, password, likes) VALUES(%s, %s, %s, %s, %s);", (name, email, username, password, 0,))
            # Save the connection
            connection.commit()
            session['logged_in'] = True
            session['username'] = username
            next_page = request.args.get('next')
            if not next_page or url_parse(next_page).netloc != '':
                flash('You are now logged in', 'success')
                next_page = url_for('profile')
            return redirect(next_page)

        # Close the connection
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
        result = cur.execute("SELECT * FROM users WHERE username = %s;", (username,))

        if result > 0:
            # Get stored hash
            data = cur.fetchone()
            password = data['password']

            # Compare passwords
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

""" Logout """


@app.route('/logout')
def logout():
    session.clear()
    flash('You are now logged out', 'success')
    return redirect(url_for('login'))

""" Profile """


@app.route('/profile', methods=['GET', 'POST'])
def profile():
    form = EditForm(CombinedMultiDict((request.files, request.form)))
    # Create cursor
    cur = connection.cursor()

    # Get session username
    user = session.get('username')
    date = datetime.utcnow()

    # Get current username details from db
    cur.execute("SELECT name, email, aboutme, image FROM users  WHERE username = %s;", (user,))
    user_details = cur.fetchall()
    current_name = user_details[0].get('name')
    current_email = user_details[0].get('email')
    profile_description = user_details[0].get('aboutme')
    image_file = user_details[0].get('image')
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
        picture_path = os.path.abspath(os.path.join('app/static/images', new_picture_fn))
        output_size = (180, 180)

        i = Image.open(picture)
        i.thumbnail(output_size)

        i.save(picture_path)
        picture_file = new_picture_fn

        # Get session username
        user = session.get('username')

        # Create cursor
        cur = connection.cursor()

        # Get current username and email from db
        cur.execute("SELECT name, email FROM users  WHERE username = %s;", (user,))
        result = cur.fetchall()
        current_name = result[0].get('name')
        current_email = result[0].get('email')

        # Check the name and email that come from the form to make sure everything is updated correctly

        get_db_name = cur.execute("SELECT name FROM users WHERE name = %s;", (name,))
        get_db_email = cur.execute("SELECT email FROM users WHERE email = %s;", (email,))

        if name != current_name:
            if get_db_name > 0:
                flash("That name is already taken. Please choose a different one.", 'danger')
            elif (get_db_email > 0 and email != current_email):
                flash("That email is already taken. Please choose a different one.", 'danger')
            else:
                cur.execute("UPDATE users SET name = %s, email = %s, aboutme = %s, image = %s WHERE username = %s;", (name, email, about_me, picture_file, user,))
                flash('Your profile has been updated successfully', 'success')
                return redirect(url_for('profile'))
        elif email != current_email:
            if get_db_email > 0:
                flash("That email is already taken. Please choose a different one.", 'danger')
            elif (get_db_name > 0 and form.name.data != current_name):
                flash("That name is already taken. Please choose a different one.", 'danger')
            else:
                cur.execute("UPDATE users SET name = %s, email = %s, aboutme = %s, image = %s WHERE username = %s;", (name, email, about_me, picture_file, user,))
                flash('Your profile has been updated successfully', 'success')
                return redirect(url_for('profile'))
        else:
            flash('Your profile has been updated successfully', 'success')
            cur.execute("UPDATE users SET aboutme = %s, image = %s WHERE username = %s;", (about_me, picture_file, user,))
            return redirect(url_for('profile'))
        # Commit and close the connection
        connection.commit()
        cur.close()

    # Implement pagination for user recipes
    pagination_offset = int(request.args.get('offset', '0'))
    pagination_limit = int(request.args.get('limit', '6'))
    user_made = user_recipes.find({"username": user})
    if user_made.count() > 0:
        starting_id = user_made.sort('_id', pymongo.ASCENDING)
        last_id = starting_id[pagination_offset]['_id']
        total_results = 0
        total_results = len([total_results + 1 for recipe in user_made])

        args = {
            "limit": pagination_limit,
            "offset": pagination_offset,
            "recipes_sorted": user_recipes.find({"$and": [{"username": user}, {'_id': {'$gte': last_id}}]})
                                          .sort('_id', pymongo.ASCENDING)
                                          .limit(pagination_limit),
            "next_url": '/profile?limit=' + str(pagination_limit) + '&offset=' + str(pagination_offset + pagination_limit),
            "prev_url": '/profile?limit=' + str(pagination_limit) + '&offset=' + str(pagination_offset - pagination_limit),
            "recipes": user_made,
            "total_results": total_results
        }

        return render_template('profile.html', args=args, user_made=user_made,
                               current_name=current_name,
                               image_file=image_file,
                               date=date, current_email=current_email,
                               profile_description=profile_description,
                               form=form)
    else:
        return render_template('profile.html', current_name=current_name,
                               image_file=image_file, date=date,
                               current_email=current_email,
                               profile_description=profile_description,
                               form=form)

""" Get all recipes and implement pagination """


@app.route('/recipes', methods=['GET', 'POST'])
def recipes():

    pagination_offset = int(request.args.get('offset', '0'))
    pagination_limit = int(request.args.get('limit', '6'))

    recipes = recipe_collection.find()
    starting_id = recipe_collection.find().sort('_id', pymongo.ASCENDING)
    last_id = starting_id[pagination_offset]['_id']
    total_results = 0
    total_results = len([total_results + 1 for item in recipes])

    args = {
        "limit": pagination_limit,
        "offset": pagination_offset,
        "recipes_sorted": recipe_collection.find({'_id': {'$gte': last_id}})
                                           .sort('_id', pymongo.ASCENDING)
                                           .limit(pagination_limit),
        "next_url": '/recipes?limit=' + str(pagination_limit) + '&offset=' + str(pagination_offset + pagination_limit),
        "prev_url": '/recipes?limit=' + str(pagination_limit) + '&offset=' + str(pagination_offset - pagination_limit),
        "recipes": recipes,
        "total_results": total_results
    }
    return render_template('recipes.html', cuisines=mongo.db.cuisines.find(),
                           courses=mongo.db.courses.find(),
                           allergens=mongo.db.allergens.find(), args=args)

""" Get the filter results for recipes and then
    implement pagination for filter results """


@app.route('/filter_recipes', methods=["GET", "POST"])
def filter_recipes():
    result = []
    filter_result = []
    if request.method == 'POST':
        form = request.form.to_dict()
        session['filter_form'] = form
        recipes = dumps(recipe_collection
                        .aggregate([{"$match": {"$and": get_results(form)}}]))
        filter_result = json.loads(recipes)
        session['count_filter'] = str(len([x for x in filter_result]))
        count_filter = session['count_filter']

    # Pagination on GET request for filters
    pagination_offset = int(request.args.get('offset', '0'))
    pagination_limit = int(request.args.get('limit', '6'))
    form = session.get('filter_form')
    count_filter = session.get('count_filter')

    starting_id = recipe_collection.aggregate([{"$match": {"$and": get_results(form)}},
                                               {"$sort": {"_id": 1}}])
    results_count = 0
    for count_item in starting_id:
        results_count += 1
        result.append(count_item)

    if results_count != 0:
        last_id = result[pagination_offset]['_id']
        args = {
            "limit": pagination_limit,
            "offset": pagination_offset,
            "recipes_sorted": recipe_collection.aggregate([{"$match": {"$and": [{"$and": get_results(form)},
                                                           {"_id": {"$gte": last_id}}]}},
                                                           {"$sort": {"_id": 1}},
                                                           {"$limit": pagination_limit}]),
            "next_url": '/filter_recipes?limit=' + str(pagination_limit) +
                        '&offset=' + str(pagination_offset + pagination_limit),
            "prev_url": '/filter_recipes?limit=' + str(pagination_limit) +
                        '&offset=' + str(pagination_offset - pagination_limit),
            "total_results": results_count
        }

        cuisines = mongo.db.cuisines.find()
        courses = mongo.db.courses.find()
        allergens = mongo.db.allergens.find()
        return render_template('recipes.html', count_filter=count_filter,
                               form=form, cuisines=cuisines,
                               courses=courses, allergens=allergens,
                               args=args)
    else:
        cuisines = mongo.db.cuisines.find()
        courses = mongo.db.courses.find()
        allergens = mongo.db.allergens.find()
        return render_template('recipes.html', cuisines=cuisines,
                               courses=courses, allergens=allergens,
                               count_filter=count_filter)

""" Get the number of filter results for recipes """


@app.route('/filter_results/<allergen>/<cuisine>/<course>',
           methods=['POST'])
def filter_results(allergen, cuisine, course):
    if request.method == 'POST':
        recipes = []
        if allergen == 'None' and cuisine == 'None':
            recipes = dumps(recipe_collection
                            .find({'course_name': course}))
        elif allergen == 'None' and course == 'None':
            recipes = dumps(recipe_collection
                            .find({'cuisine_name': cuisine}))
        elif course == 'None' and cuisine == 'None':
            recipes = dumps(recipe_collection
                            .find({'allergen_name': allergen}))
        elif allergen == 'None' and cuisine != 'None' and course != 'None':
            recipes = dumps(recipe_collection
                            .aggregate([{"$match":
                                         {"$and": [{"cuisine_name": cuisine},
                                          {"course_name": course}]}}]))
        elif cuisine == 'None' and allergen != 'None' and course != 'None':
            recipes = dumps(recipe_collection
                            .aggregate([{"$match":
                                         {"$and": [{"allergen_name": allergen},
                                          {"course_name": course}]}}]))
        elif course == 'None' and allergen != 'None' and cuisine != 'None':
            recipes = dumps(recipe_collection
                            .aggregate([{"$match":
                                         {"$and": [{"allergen_name": allergen},
                                          {"cuisine_name": cuisine}]}}]))
        else:
            recipes = dumps(recipe_collection
                            .aggregate([{"$match":
                                         {"$and": [{"allergen_name": allergen},
                                          {"cuisine_name": cuisine},
                                          {"course_name": course}]}}]))
        filter_result = json.loads(recipes)
        count_recipes = str(len([x for x in filter_result]))
        return count_recipes

""" Get the search results for recipes and then
    implement pagination for search results """


@app.route('/search_recipes', methods=['GET', 'POST'])
def search_recipes():
    result = []
    parsed_result = []
    if request.method == 'POST':

        # Get the results from the form according to user input
        search_text = request.form.get('search_input')
        session['search_text'] = search_text
        result = dumps(recipe_collection
                       .find({"$text": {"$search": str(search_text)}}))
        parsed_result = json.loads(result)

        session['count_recipes'] = str(len([x for x in parsed_result]))
        count_recipes = session['count_recipes']

    # Pagination for search on GET request
    pagination_offset = int(request.args.get('offset', '0'))
    pagination_limit = int(request.args.get('limit', '6'))
    search_text = session.get('search_text')
    count_recipes = session.get('count_recipes')

    recipes = recipe_collection.find({"$text": {"$search": str(search_text)}})
    starting_id = recipe_collection.find({"$text": {"$search": str(search_text)}}).sort('_id', pymongo.ASCENDING)
    results_count = starting_id.count()

    if results_count != 0 and search_text is not None:
        last_id = starting_id[pagination_offset]['_id']
        total_results = 0
        total_results = [total_results + 1 for item in recipes]
        args = {
            "limit": pagination_limit,
            "offset": pagination_offset,
            "recipes_sorted": recipe_collection.find({"$and": [{"$text": {"$search": str(search_text)}}, {'_id': {'$gte': last_id}}]})
                                               .sort('_id', pymongo.ASCENDING)
                                               .limit(pagination_limit),
            "next_url": '/search_recipes?limit=' + str(pagination_limit) + '&offset=' + str(pagination_offset + pagination_limit),
            "prev_url": '/search_recipes?limit=' + str(pagination_limit) + '&offset=' + str(pagination_offset - pagination_limit),
            "total_results": len(total_results)
        }

        return render_template('search_recipes.html',
                               count_recipes=count_recipes,
                               search_text=search_text,
                               args=args)
    else:
        return render_template('search_recipes.html',
                               count_recipes=count_recipes,
                               search_text=search_text)

""" Get the number of search results for recipes """


@app.route('/search_results/<search_input>', methods=['POST'])
def search_results(search_input):
    if request.method == 'POST':
        result = recipe_collection.find({"$text": {"$search": str(search_input)}})
        count_recipes = str(result.count())
        return count_recipes

""" Allow logged in user to add recipe """

@login_required
@app.route('/add_recipe', methods=['GET', 'POST'])
def add_recipe():
    user = session.get('username')
    if user:
        return render_template('add_recipe.html',
                               user_recipes=mongo.db.user_recipes.find(),
                               courses=mongo.db.courses.find(),
                               cuisines=mongo.db.cuisines.find(),
                               allergens=mongo.db.allergens.find())
    else:
        return redirect(url_for('login'))

""" Allow user to cancel editing a recipe """

@login_required
@app.route('/cancel_edit_recipe/<recipe_id>', methods=['GET'])
def cancel_edit_recipe(recipe_id):
    recipe = user_recipes.find_one({"_id": ObjectId(recipe_id)})
    return render_template('get_user_recipe.html', user_recipe=recipe)

""" Insert a recipe in the user_recipe collection """

@login_required
@app.route("/insert_recipe", methods=["POST"])
def insert_recipe():
    if request.method == 'POST':
        form = request.form.to_dict()
        instructions = []
        ingredients = []

        # Loop through the keys in the form
        # If the key matches instruction append
        # instruction to instructions list
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
            "course_name": request.form.get("course_name"),
            "recipe_name": request.form.get("recipe_name"),
            "recipe_image": "https://media.self.com/photos/58f7d022feead55f43f7fc78/4:3/w_728,c_limit/Creamy-Sun-Dried-Parmesan-Chicken-cafedelites-1%25202.jpg",
            "username": session.get("username")
        })

    flash("Your recipe has been added successfully. Please note that you can not like/rate your own recipes.", "success")
    return redirect(url_for('profile'))

""" Edit user recipe """

@login_required
@app.route("/edit_recipe/<recipe_id>")
def edit_recipe(recipe_id):
    user = session.get('username')
    if user:
        the_recipe = user_recipes.find_one({"_id": ObjectId(recipe_id)})
        return render_template("edit_recipe.html", the_recipe=the_recipe,
                           cuisines=mongo.db.cuisines.find(),
                           allergens=mongo.db.allergens.find(),
                           courses=mongo.db.courses.find())
    else:
        return redirect(url_for('login'))

""" Update user recipe """

@login_required
@app.route("/update_recipe/<recipe_id>", methods=["POST"])
def update_recipe(recipe_id):
    user = session.get('username')
    if user:
        form = request.form.to_dict()
        instructions = []
        ingredients = []
    
        # Loop through the keys in the form
        # If the key matches instruction append
        # instruction to instructions list
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
                            {'username': session.get("username"),
                             'recipe_image': "https://media.self.com/photos/58f7d022feead55f43f7fc78/4:3/w_728,c_limit/Creamy-Sun-Dried-Parmesan-Chicken-cafedelites-1%25202.jpg",
                             'recipe_name': request.form.get('recipe_name'),
                             'allergen_name': request.form.get('allergen_name'),
                             'cuisine_name': request.form.get('cuisine_name'),
                             'course_name': request.form.get('course_name'),
                             'instructions': instructions,
                             'ingredients': ingredients})
        flash("Your recipe has been updated successfully", "success")
        return redirect(url_for('get_user_recipe', recipe_id=recipe_id))
    else:
        return redirect(url_for('login'))

""" Delete user recipe """

@login_required
@app.route('/delete_recipe/<recipe_id>')
def delete_recipe(recipe_id):
    user = session.get('username')
    if user:
        user_recipes.remove({'_id': ObjectId(recipe_id)})
        flash('Your recipe has been deleted successfully', 'success')
        return redirect(url_for('profile'))
    else:
        return redirect(url_for('login'))

""" View details of a user recipe """

@login_required
@app.route('/get_user_recipe/<recipe_id>', methods=['GET', 'POST'])
def get_user_recipe(recipe_id):
    user = session.get('username')
    if user:
        user_recipe = user_recipes.find_one({"_id": ObjectId(recipe_id)})
        return render_template("get_user_recipe.html", user_recipe=user_recipe)
    else:
        return redirect(url_for('login'))

""" View details of a database recipe """


@app.route('/get_recipe/<recipe_id>', methods=['GET', 'POST'])
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
            regex_string = "(^(clove|cup|teaspoon|tablespoon|\d(?<!-)$|ounce|inch|pound|pinch|slices?(?<!d)$|milliliter)|.\d)"
            regex = re.findall(regex_string, firstElement)
            if regex:
                concatenated_quantity += "{} ".format(ingredientSplit[i])
            else:
                concatenated_ingredient += "{} ".format(ingredientSplit[i])
            i += 1
        full_quantities.append(concatenated_quantity)
        full_ingredients.append(concatenated_ingredient)

    """ Get the rating text for each rating done by each user for each recipe
        and check for user None value """

    user = session.get('username')
    recipe_number = the_recipe["id"]

    instance_rating = []
    if user is not None:
        # Get MySQL connection
        cur = connection.cursor()
        cur.execute("SELECT id FROM users WHERE username = %s;", (user,))
        user_id = cur.fetchall()[0]['id']
        instance_like = cur.execute("SELECT * FROM userlikes WHERE userId = %s AND recipeId = %s;", (user_id, recipe_number,))
        if instance_like == 0:
            cur.execute("INSERT INTO userlikes(userId, recipeId) VALUES(%s, %s);", (user_id, recipe_number))
        connection.commit()
        cur.close()

        instance_rating = ratings_collection.find_one({"user_id": user_id,
                                                       "recipe_id": recipe_number})
        if instance_rating is None:
            ratings_collection.insert_one({"user_id": user_id,
                                           "recipe_id": recipe_number,
                                           "rating": "0",
                                           "rateText": "Rate Recipe"})
    else:
        return render_template('get_recipe.html', user=user,
                               recipe=the_recipe, total=total,
                               full_quantities=full_quantities,
                               full_ingredients=full_ingredients)
    return render_template('get_recipe.html', user=user, recipe=the_recipe,
                           total=total, full_quantities=full_quantities,
                           full_ingredients=full_ingredients,
                           instance_rating=instance_rating)

""" Like recipe """


@app.route('/like/<recipe_id>', methods=['GET', 'POST'])
def like(recipe_id):

    # Get MySQL connection
    cur = connection.cursor()

    # Get variables
    user = session['username']
    recipe = recipe_collection.find_one({"_id": ObjectId(recipe_id)})
    recipe_number = recipe["id"]
    likes = recipe["likes"]
    dislikes = recipe["dislikes"]

    """ Check if a record with the session user and the recipe
    exists in the userlikes table from the database.
    If it does not then insert the new record into
    the user likes table
    Get the liked flag and check if it's 0 or 1.
    If it's 1 then update the number of likes.
    Finally, set the liked flag to 0 so a recipe can
    not be liked anymore.
    Commit to the database and redirect.
    """
    cur.execute("SELECT id FROM users WHERE username = %s;", (user,))
    user_id = cur.fetchall()[0]['id']
    cur.execute("SELECT liked FROM userlikes WHERE userId = %s AND recipeId = %s;", (user_id, recipe_number,))
    liked_flag = cur.fetchall()[0]['liked']
    cur.execute("SELECT count_liked FROM userlikes WHERE userId = %s AND recipeId = %s;", (user_id, recipe_number,))
    count_liked = cur.fetchall()[0]['count_liked']
    if liked_flag == 1:
        if count_liked == 0:
            likes = likes + 1
        elif count_liked > 0 and dislikes != 0:
            likes = likes + 1
            dislikes = dislikes - 1
        recipe_collection.update({'_id': ObjectId(recipe_id)}, {
                                  "$set": {"likes": likes, "dislikes": dislikes}})
        cur.execute("UPDATE userlikes SET liked = '0', unliked = '1', count_liked = 1 WHERE userId = %s AND recipeId = %s;", (user_id, recipe_number,))
        connection.commit()
    cur.close()
    
    if user:
        return json.jsonify({'likes': likes, 'dislikes': dislikes, 'recipe_id': recipe_id})
    else:
        return redirect(url_for('login'))

""" Dislike recipe """


@app.route('/dislike/<recipe_id>', methods=['GET', 'POST'])
def dislike(recipe_id):
    # Get MySQL connection
    cur = connection.cursor()

    # Get variables
    user = session['username']
    recipe = recipe_collection.find_one({"_id": ObjectId(recipe_id)})
    recipe_number = recipe["id"]
    likes = recipe["likes"]
    dislikes = recipe["dislikes"]

    """ Check if a record with the session user and the
    recipe exists in the userlikes table from the database.
    If it does not then insert the new record into
    the user likes table.
    Get the unliked flag and check if it's 0 or 1.
    If it's 1 then update the number of likes.
    Finally, set the unliked flag to 0 so a recipe
    can not be disliked anymore.
    Commit to the database and redirect.
    """
    cur.execute("SELECT id FROM users WHERE username = %s;", (user,))
    user_id = cur.fetchall()[0]['id']
    cur.execute("SELECT unliked FROM userlikes WHERE userId = %s AND recipeId = %s;", (user_id, recipe_number,))
    unliked_flag = cur.fetchall()[0]['unliked']
    cur.execute("SELECT count_liked FROM userlikes WHERE userId = %s AND recipeId = %s;", (user_id, recipe_number,))
    count_liked = cur.fetchall()[0]['count_liked']
    if unliked_flag == 1:
        if count_liked == 0:
            dislikes = dislikes + 1
        elif count_liked > 0 and likes != 0:
            dislikes = dislikes + 1
            likes = likes - 1
        recipe_collection.update({'_id': ObjectId(recipe_id)}, {
                                  "$set": {"likes": likes, "dislikes": dislikes}})
        cur.execute("UPDATE userlikes SET unliked = '0', liked = '1', count_liked = 1 WHERE userId = %s AND recipeId = %s;", (user_id, recipe_number,))
        connection.commit()
    cur.close()
    
    if user:
        return json.jsonify({'likes': likes, 'dislikes': dislikes, 'recipe_id': recipe_id})
    else:
        return redirect(url_for('login'))

"""  Get ratings from users and store them in the database
     then return the average rating for a recipe"""


@app.route('/update_rating/<recipe_id>', methods=['GET', 'POST'])
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

        cur.execute("SELECT id FROM users WHERE username = %s;", (user,))
        user_id = cur.fetchall()[0]['id']

        instance_record = ratings_collection.find_one({"user_id": user_id, "recipe_id": recipe_number})
        if instance_record is not None:
            ratings_collection.update({"user_id": user_id, "recipe_id": recipe_number},
                                      {"$set": {"rating": rating}})
            ratings_collection.update({"user_id": user_id, "recipe_id": recipe_number},
                                      {"$set": {"rateText": "Edit Rating"}})
        else:
            ratings_collection.insert_one({"user_id": user_id, "recipe_id": recipe_number, "rating": rating})
        instance_recipe = ratings_collection.find({"recipe_id": recipe_number})
        instance_count = ratings_collection.count_documents({"recipe_id": recipe_number, "rating": {"$ne": "0"}})
        sum_rating = 0
        sum_rating = sum([sum_rating + int(doc["rating"]) for doc in instance_recipe if doc["rating"] != "0"])
        average_rating = sum_rating / instance_count
        if average_rating not in numbers_array:
            formatted_average = "{:.1f}".format(average_rating)
        else:
            formatted_average = int(average_rating)
        recipe_collection.update({"_id": ObjectId(recipe_id)},
                                 {"$set": {"rating": formatted_average}})
    if user:
        return redirect(url_for('get_recipe', recipe_id=recipe_id))
    else:
        return redirect(url_for('login'))

""" Recipe statistics """


@app.route('/statistics')
def statistics():
    return render_template('statistics.html', dot_chart=Graphs.dot_chart(),
                           solid_gauge_chart=Graphs.solid_gauge_chart(),
                           gauge_chart=Graphs.gauge_chart())

""" Handle error 404 """


@app.errorhandler(404)
def page_not_found(error):
    return render_template('error404.html'), 404

""" Handle error 405 """


@app.errorhandler(405)
def method_not_allowed(error):
    return render_template('error405.html'), 405

""" Handle database error """


@app.errorhandler(500)
def server_error(error):
    return render_template('error500.html'), 500