# Relish - A CookBook Adventure

## User Experience Design(UXD)

### Overview

Relish is a website that is desi

### What is this website for?

BulletTravel is an imaginary travel agency website to attract customers that want to enjoy their holiday with their family. 
It offers a series of travel packages along with places that can be visited. Not only does it allow users to search for places to visit, but
it also allows them to find accommodation, places to eat, tourist attractions and points of interest.
The website also allows users to send emails for project requests via the contact form.

### How does it work?

The website uses HTML and HTML5 markup language to put the structure of the website in place. It also uses CSS and Bootstrap to style 
the website. Javascript and jQuery have helped to the functionality of the website by allowing website visitors to toggle the menu and resize it when viewed in mobile, to find different places based on a change
function and to send emails via the contact form. Furthermore, these technologies allow those interested in the BulletTravel agency
to find particular destinations on Google Maps and to search for accommodation, hotels, restaurants, points of interest etc.
The website can be viewed [here](https://ioanhadarean.github.io/Interactive-Front-End-Milestone-Project/).

### User Stories
1. The *`index`* route directs the user to all the recipes
2. The *`register`*

### Wireframe

<a href="https://imgbb.com/"><img src="https://image.ibb.co/h8dRfA/Bullet-Travel.png" alt="Bullet-Travel" border="0"></a>


### Existing Features and Functionalities
The application consists of 14 HTML templates, 15 CSS files, 17 JavaScript files, 1 utility written in JavaScript
and 6 Python files, including the env file which stores the environment variables and connection strings and 
[tests.py](/zapp/tests.py), which incorporates automated tests used to measure the performance and behaviour of the project.
The main [app.py](../master/app.py) file includes a collection of all the functions and routes that have been used for
creating the logics of the website. The [models.py](/zapp/models.py) file incorporates the scripts that have been used for
the creating the statistics charts created in [Pygal](http://pygal.org/en/stable/), which is a Python library for designing
and creating charts. Last but not least, the [values.py](/zapp/values.py) file was used for modifying the point dimensions from the statistics page.
Finally, the [helpers.py](/zapp/helpers.py) file has been used for returning the dictionary that has been used for filtering recipes.

#### Website Pages
1. [Register Page](/templates/register.html)
* Consists of a form that allows the user to create an account.
* It's constructed following a defensive design, each of the fields in the register form
will produce an inline error if the required checks are not met (For example: Passwords do not match).
* If the username or the email are already in the database, the user can not register to the website.
* When clicking register, the user is automatically redirected to the profile page, without having to go through login
* The form fields are required, so an empty form can not be submitted.
* The form checks are achieved using a class named RegisterForm, created with the help of 
[Flask-WTF](https://flask-wtf.readthedocs.io/en/stable/) and [WTForms](https://wtforms.readthedocs.io/en/stable/).
2. [Login Page](/templates/login.html)
* Has a form that allows the user to login to the website.
* It's constructed following a defensive design, each of the fields in the login form
will produce an error if the required checks are not met( if the user entered the wrong password
the error will be invalid login| if the user does not exist in the database the error shown will be invalid login).
* The form fields are required, so an empty form can not be submitted.
* When clicking login, the user is automatically redirected to the profile page.
3. [Profile Page](/templates/profile.html)
* Allows the logged in user to update his profile
* The update profile form is constructed following a defensive design, each of the fields 
in the login form will produce an error if the required checks are not met, except the about me field
(for example if the user does not choose a png, jpeg or jpg file, an error is rendered below the input file field)
* The form checks are achieved using a class named EditForm, created with the help of 
[Flask-WTF](https://flask-wtf.readthedocs.io/en/stable/) and [WTForms](https://wtforms.readthedocs.io/en/stable/)
* The local date is shown on each user's profile.
* When clicking the update button, the user's profile is automatically updated, provided there are no errors.
* When clicking the cancel button, a modal opens asking the user for confirmation (if the users clicks reset progress
the form is resetted, if the user clicks continue he/she can proceed to updating his/her profile).
* The recipe cards for each user are shown on the profile page.
* If the user clicks on the edit recipe button she/he will be redirected to the edit page for that specific recipe.
* If the user clicks on the delete button, the recipe will be deleted from the page and from the database.
* If the user clicks on the recipe image or the view recipe button, she/he will be redirected to the view
for that specific recipe.
4. [Recipes Page](/templates/recipes.html)
* It has a form with three selects that allow the user to filter recipes by a combination of three: 
allergens, cuisines and courses.
* The filter results are shown on active input, the recipe container is cleared
when the select options change.
* When clicking the filter recipes button, the corresponding recipes are shown according to the filters,
as well as the number of results. 
* Users can go back to all recipes at any time by clicking the all recipes button.
* User can navigate through the recipes with the help of pagination, which is implemented
both for all recipes and the filtered recipes. ( 6 recipes per pagination page)
* The filter button is disabled, unless the user clicks on a filter.
* The header welcome message changes every time the user accesses or refreshes the page.
* If a user clicks on the image of the recipe or the view recipe button, he/she is redirected to the
view for that specific recipe.
* All users can view the recipes page and filter through recipes, regardless if they are logged in or not.
5. [Search Page](/templates/search_recipes.html)
* It has an input that allows users to search recipes when clicking on the search button.
* The number of results are shown on active input, as well as after clicking the search button.
* All users can view the search page and search recipes, logged in or not.
* The search button is disabled if the input is empty or if the input has less than three characters.
The input is also trimmed of white spaces.
* The recipe container is cleared on input change.
* Users can go back to all recipes at any time by clicking the all recipes button.
* Pagination is implemented for the search recipes results. (6 recipes per pagination page)
* If a user clicks on the image of the recipe or the view recipe button, he/she is redirected to the
view for that specific recipe.
6. [Statistics Page](/templates/statistics.html)
* Has three graphs that have been constructed with the help of functions existent in the 
[models.py](/zapp/models.py) Python file.
* The first graph (dot chart) shows the recipe statistics ingredients per cuisine. That is explained by how
many recipes from a specific cuisine contain egg, milk, sugar, flour, salt, water, garlic, vanilla or butter.
(For example: 2 out of 4 French recipes contain egg).
* The second graph (solid gauge chart) illustrates the recipes allergens statistics in %. (For example: the garlic
allergen is found in 41.66% of the recipes.)
* The third graph (gauge chart) displays the average calories by cuisine. (For example: the Greek cuisine has an average
of 599 calories)
* Logged in or not, all users can look at the statistics page.
7. [Database Recipe Page](/templates/get_recipe.html)
* When a user who is not logged in clicks on like/dislike or rate recipe button, a modal pops up which requires the user
to login if he/she has an account or to register if he/she does not have an account.
* It is important to mention that the user is redirected back 


### Features Left To Implement

1. SVG can be added as a feature because -webkit-text-stroke-width doesn't work in Internet Explorer.
2. Minor fixes can be made to make the website look pixel perfect.

## Bugs Fixed

1. When a user types a location in the empty fieldbox and wants to select a different country, 
the location does not clear out(fixed with an eventListener function that would clear out the
location field when a new country is selected).
2. When a user clicks on a radio button, the markers and locations are shown on the map even if 
the location is not selected(fixed with a function that would enable the radio buttons when the
length of the autocomplete string is more than 0).
3. When the contact form is about to be submitted, the form does not reset. Therefore, the user does
not know if the email was sent or not and he could spam a lot of emails(fixed by adding an alert
mentioning if the email was sent or not and a reset for the contact form).
4. When a user clicks on a place type and that place type does not exist for that specific location, the results 
and markers from the previous place don't clear out(fixed by adding clearMarkers() and markers = []
after each time a radio button changes its value).
5. When a user clicks on another country, the markers from the previous country don't clear out(fixed by
adding a function that clears markers after each time another country is clicked).

## Tech Used

### Front-End Technologies

1. **HTML**, **CSS** and **JavaScript**
    <br>Languages that were used to improve the feel of the Relish website. Pure HTML and CSS was predominantly
    used for designing the recipe views. Note: no jQuery was used for this
    project because the intention to improve the learning curve with vanilla JavaScript.
2. **Bootstrap v3.3.7**(https://getbootstrap.com/docs/3.3/getting-started/#download)
    <br>**Bootstrap** was used to give the project a responsive layout. The original intention was to not use 
    any HTML and CSS libraries in order to make the website from scratch. However, that would have taken a lot of
    time so in the end it all came to a mix of libraries for web design and pure HTML and CSS.
3. **Font Awesome v4.7.0**(https://stackpath.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css)
    <br>**Font Awesome v5.3.1**(https://use.fontawesome.com/releases/v5.3.1/css/all.css)
    <br>Font and icon toolkits based on CSS and LESS that were used to style the website.
4. **Ionic Framework**(https://ionicframework.com)
    <br>**Ionic Framework** was used for a few icons.
5. **Uikit**(https://getuikit.com/docs/introduction)
    <br>**Uikit** was used mostly for the forms that sent the data.


### Back-end Technologies
1. **Python**(https://www.python.org)
   <br>**Python** is a powerful programming language that is used to build websites in a 
   relatively short amount of time.
2. **Flask**(http://flask.pocoo.org)
   <br>**Flask** is a Python microframework that was used to construct the functionalities of the website.
3. **PyMongo 3.7.2**(https://api.mongodb.com/python/current/)
   <br>**PyMongo 3.7.2** is a Python library that made the connection between Flask and the mLab MongoDB database.
   Note:  The command that was run for finding the version of pymongo was *pip freeze | grep pymongo*
4. **PyMySQL**(https://pymysql.readthedocs.io/en/latest/)
   <br>**PyMySQL** is a Python library that liaised MySQL with Flask and Python.
   Note:  The command that was run for finding the version of pymongo was *pip freeze | grep PyMySQL*




## Database Schema
Two types of database were used in the creation of this project: a non-relational (NOSQL) database and a relational database(MYSQL).
1. NOSQL database - [MongoDB](https://mlab.com/welcome/) - was used for storing the information related to the recipes, including the
connections with MYSQL that were constructed with the Python logic. The recipe database consists of six collections:
* allergens\
    Each allergen has an *`_id`*(object) and an *`allergen_name`*(string). There are 4 allergens in the collection:
    * egg
    * milk
    * garlic
    * nuts
* courses\
    Each course has an *`_id`*(object) and a *`course_name`*(string). There are 5 courses in the collection:
	* appetizer
	* soup
	* dinner
	* dessert
	* main dish
* cuisines\
    Each cuisine has an *`_id`*(object) and a *`cuisine_name`*(string). There are 8 cuisines in the collection:
    * Mexican
	* French
	* Asian
	* Italian
	* Greek
	* Irish
	* Indian
	* English
* ratings\
    Each rating has the following keys:
	* _id(object)
	* rateText(string)
	* user_id(string)
	* rating(string)
	* recipe_id(string)
    Note: rateText is initially set to *`Rate Recipe`* and it changes to *`Edit Rating`* when the user already rated a recipe
* recipes\
    There are 24 database recipes. Each recipes has the following keys:
    * _id(object)
    * id(string)
    * recipe_name(string)
    * recipe_image(string)
    * cuisine_name(string)
    * course_name(string)
    * allergen_name(string)
    * ingredients(array)
    * cooking_directions(array)
    * author_name(string)
    * preparation_time(string)
    * cooking_time(string)
    * servings(string) 
    * calories(string) 
    * likes(int) - initially set to 0
    * rating(int) - initially set to 0/ or to the initial recipe rating
2. MySQL database - [JawsDB](https://www.jawsdb.com) - was used for storing the information related to the users, including the
connections with MYSQL that were constructed with the Python logic. It consists of 2 tables:
* users
* userlikes\
For more information about MySQL database schema please refer to the [flaskapp.sql](../master/flaskapp.sql) script.




## Testing

1. Prototype code was written and tested using Cloud9 and Chrome Developer Tools.
2. All HTML and CSS code used on the site has been tested using [The W3 CSS Validation Service](https://jigsaw.w3.org/css-validator/) 
            and [The W3 Markup Validation Service](https://validator.w3.org/).
3. All Javascript and jQuery code on the website has been tested using [JSHint](https://jshint.com/).
4. Site viewed and tested in the following browsers(including toggle functionality, filtering type places and using Google Maps):
<br>    i Google Chrome
<br>    ii Mozilla Firefox
<br>    iii Opera
<br>    iv Internet Explorer
5. Postman was used for sending GET and POST requests to the website in order to test it




## Deployment
Note: the coding for the project was done in Cloud9. 
1. Created a new git repository by typing *`git init`* in the terminal.
2. Added the git remote by typing *`git remote add origin https://github.com/IoanHadarean/CookBook-project.git`* in the CLI.
3. Created a requirements.txt file using *`(sudo) pip3 freeze --local > requirements.txt`*. This file was necessary for the deployment process
since it allowed Heroku to figure out what packages should be installed when deploying the app on the production server.
4. Created a Procfile that declared the type of application, in this case a web application. The command used for initialising the Procfile
was *`echo web: python app.py > Procfile`*.
5. Logged in to [Heroku](https://www.heroku.com/home) by typing *`heroku login`* in the terminal. 
6. Pushed the code from git master branch to Heroku by using the following command:
*`git push heroku master`*.
Note: Heroku is a cloud-based platform that makes it easy to deploy and scale Python apps, regardless if the framework used is
Flask or Django.
7. Added the config variables to Heroku in the settings option:


| Key      | Value          |
| ------------- |:-------------:|
|  *`JAWSDB-DATABASE-URL`* |                       |
|      *`DBHOST`*           |                       |
|      *`DBPASS`*           |                       |
|        *`DBNAME`*         |                       |
|     *`DBUSERNAME`*        |                       |
|          *`IP`*           |                       |
|        *`PORT`*           |                       |
|     *`SECRET_KEY`*        |                       |
|        *`MONGO_URI`*      |                       |
|       *`MONGO_DBNAME`*    |                       |
8. Exported the local database to Heroku by using the free JawsDB add-on provided by the platform.
9. Dumped all the MYSQL scripts that were used for creating the *`flaskapp`* database locally by running 
*`mysqldump -u $C9_USER -p flaskapp > flaskapp.sql`* in the CLI.
10. Connected to the JawsDB database by typing *`mysql -u username -h JawsDBhost -p JawsDBname `* in the terminal.
11. Ran the scripts from [flaskapp.sql](../master/flaskapp.sql) into MySQL terminal to repopulate the data.



### Getting the code up and running
The project runs on a production server called Heroku. If you want to run the project locally please follow these instructions.
Note the fact that you would need to contact the app administrator in order to get the connection details that were used in the construction
of this app.
1. Download and install Python3 via the Command Line Interface(CLI) (Make sure you are using Python3, the project won't run on Python2). 
In order to check the version of Python installed type python --version in the terminal.
2. Clone the following project using *`git clone https://github.com/IoanHadarean/CookBook-project.git`* or download it and then unzip it
3. Install the packaged needed for the project via the terminal by typing (sudo) pip3 install -r requirements.txt.
4. Add all environment variables to an env.py file that is in the following format:

Note: all connection details must be in a string format
***
```import os
os.environ["SECRET_KEY"] = SECRET
os.environ["MONGO_URI"] = "mongodb://username:password@ds136786.mlab.com:36786/database"
os.environ["MONGO_DBNAME"] = "MONGODBNAME"
os.environ["DB_USERNAME"] = 'DBUSERNAME'
os.environ["DB_HOST"] = 'DBHOST'
os.environ["DB_PASS"] =  'DBPASS'
os.environ["DB_NAME"] = 'DBNAME'
```
***
Additional Note: you don't need to import the env file as it is already imported in the project
5. Run the app by typing *`python3 app.py`* in the terminal
Note: the debug is by default set to FALSE, but you can set it to TRUE to allow debugging
Additional Note: If the editor you are working on does not have a virtual environment already set up,
you would need to create one yourself. Please refer to this documentation for creating a venv 
[Virtual Environment and Packages] (https://docs.python.org/3/tutorial/venv.html)

## Credits

I would like to thank all Code Institute Students for helping me along this project and for providing feedback. Some of those people are JoWings, ShaneMuirhead, 
JohnL3, robinz, Sean, Kevin Stewart and Sammy Dartnall, who found quite a lot of bugs in my project. Special thanks goes to my mentor Moosa Hassan for his amazing support
and guidance and to Miro_lead for the sessions that we had each Sunday covering different development topics and for his constructive criticism and feedback. I would also like
to thank Graffino(Sibiu) for offering me an internship during the time I was doing the project. The internship really helped me improve my UI speed and design skills.
I also learnt a few tricks from them such as [CSS BEM](http://getbem.com/introduction/). Even though the project does not follow the BEM standards, some of the naming 
conventions used in the project are derived from BEM.

### Media

The `images` used on this site were obtained from [Google Images](https://images.google.com/).

### Information

The information used to create this site was from [Allrecipes | Food, friends, and recipe inspiration](https://www.allrecipes.com).
