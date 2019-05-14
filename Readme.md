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


### Wireframe

<img src="relish-cookbook.png" alt="Relish-CookBook" border="0">


### Existing Features and Functionalities
The application consists of 14 HTML templates, 15 CSS files, 17 JavaScript files, 1 utility written in JavaScript
and 6 Python files, including the env file which stores the environment variables and connection strings plus
[tests.py](/zapp/tests.py), which incorporates automated tests used to measure the performance and behaviour of the project.
The main [app.py](../master/app.py) file includes a collection of all the functions and routes that have been used for
creating the logic of the website. The [models.py](/zapp/models.py) file incorporates the scripts that have been used for
the statistics charts designed with [Pygal](http://pygal.org/en/stable/), which is a Python library for designing
and creating charts. Last but not least, the [values.py](/zapp/values.py) file was used for modifying the point dimensions from 
the statistics page. Finally, the [helpers.py](/zapp/helpers.py) file has been used for returning the dictionary that has been used
for filtering recipes. Even though the initial plan was not to use any CSS frameworks, it turned out that it would take too much time
to make everything from scratch. Hence the project focused more on functionalities and it reflects a steep learning curve.



#### Website Pages + User Stories
1. [Register Page](/templates/register.html)
* Consists of a form that allows the user to create an account.
* It's constructed following a defensive design, each of the fields in the register form
will produce an inline error if the required checks are not met (For example: Passwords do not match).
* If the username or the email are already in the database, the user can not register to the website.
* When clicking register, the user is automatically redirected to the profile page, without having to go through login.
* The form fields are required, so an empty form can not be submitted.
* The form checks are achieved using a class named RegisterForm, created with the help of 
[Flask-WTF](https://flask-wtf.readthedocs.io/en/stable/) and [WTForms](https://wtforms.readthedocs.io/en/stable/).
2. [Login Page](/templates/login.html)
* Has a form that allows the user to login to the website.
* It's constructed following a defensive design, each of the fields in the login form
will produce an error if the required checks are not met( if the user entered the wrong password
the error will be invalid login, if the user does not exist in the database the error shown will be user not found).
* The form fields are required, so an empty form can not be submitted.
* When clicking login, the user is automatically redirected to the profile page.
3. [Profile Page](/templates/profile.html)
* Allows the logged in user to update his/her profile.
* The update profile form is constructed following a defensive design, each of the fields 
in the login form will produce an error if the required checks are not met, except the about me field
(For example: if the user does not choose a png, jpeg or jpg file, an error is rendered below the input file field).
* The form checks are achieved using a class named EditForm, created with the help of 
[Flask-WTF](https://flask-wtf.readthedocs.io/en/stable/) and [WTForms](https://wtforms.readthedocs.io/en/stable/).
* The local date is shown on each user's profile.
* When clicking the update button, the user's profile is automatically updated, provided there are no errors.
* When clicking the cancel button, a modal opens asking the user for confirmation (if the user clicks reset progress
the form is resetted, if the user clicks continue he/she can proceed to updating his/her profile).
* The recipe cards for each user are shown on the profile page.
* If the user clicks on the edit recipe button she/he will be redirected to the edit page for that specific recipe.
* Whenever a user clicks on the delete button, a modal pops up asking the user for confirmation(if the user clicks delete
the recipe is deleted from the database and his/her profile, if the user clicks cancel the delete modal closes).
* If the user clicks on the recipe image or the view recipe button, she/he will be redirected to the view
for that specific recipe.
4. [Recipes Page](/templates/recipes.html)
* It has a form with three selects, that allow the user to filter recipes by a combination of three: 
allergens, cuisines and courses.
* The filter results are shown on active input, the recipe container is cleared when the select options change.
* When clicking the filter recipes button, the corresponding recipes are shown according to the filters,
as well as the number of results. 
* Users can go back to all recipes at any time by clicking the all recipes button.
* Users can navigate through the recipes with the help of pagination, which is implemented
both for all recipes and the filtered recipes (6 recipes per pagination page).
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
* Pagination is implemented for the search recipes results (6 recipes per pagination page).
* If a user clicks on the image of the recipe or the view recipe button, he/she is redirected to the
view for that specific recipe.
6. [Statistics Page](/templates/statistics.html)
* Has three graphs that have been constructed with the help of functions existent in the 
[models.py](/zapp/models.py) Python file.
* The first graph (dot chart) shows the recipe statistics ingredients per cuisine. That is explained by how
many recipes from a specific cuisine contain egg, milk, sugar, flour, salt, water, garlic, vanilla or butter
(For example: 2 out of 4 French recipes contain egg).
* The second graph (solid gauge chart) illustrates the recipes allergens statistics in % (For example: the garlic
allergen is found in 41.66% of the recipes).
* The third graph (gauge chart) displays the average calories by cuisine (For example: the Greek cuisine has an average
of 599 calories).
* Logged in or not, all users can look at the statistics page.
7. [Database Recipe Page](/templates/get_recipe.html)
* When a user who is not logged in clicks on the like/dislike or rate recipe button, a modal pops up which requires the user
to login if he/she has an account or to register if he/she does not have an account.
* The user is redirected back to the recipe he was viewing after registering/logging in to the website.
* The user can view all the details of the recipe and he can also click on the add recipe button to add her/his own recipes.
* A logged in user can like and dislike a recipe the following way: when she/he clicks on the like button, the number of likes
goes up by 1, when he/she clicks on the disliked button the number of dislikes goes down by 1 (Note: the page does not refresh 
on like/dislike due to AJAX).
* When a logged in user tries to click on the rate button, a modal pops up that allows the user to fill the number of stars 
according to his/her rating. Upon clicking on save and continue, the rating is saved and the average rating for that recipe is 
updated.
* When a logged in user tries to rate a recipe, the initial rate text is set to `Rate Recipe`, but if the user tries to update
his previous rating, the rate text changes to `Edit Rating` (Note: this happens for every recipe a logged in user tries to rate).
8. [User Recipe Page](/templates/get_user_recipe.html)
* The user can view all the details of his/her recipe and he can also click on the add recipe button to add another recipe.
* If the user clicks on the edit recipe button she/he will be redirected to the edit page for her/his specific recipe.
* Whenever a user clicks on the delete button, a modal pops up asking the user for confirmation (if the user clicks delete
the recipe is deleted from the database and his/her profile and he/she is redirected to the profile page, if the user clicks cancel 
the delete modal closes).
9. [Add Recipe Page](/templates/add_recipe.html)
* It has a form that allows a user to fill the recipe name, add ingredients and instructions, as well as choose the cuisine,
course and allergen for the recipe that they are trying to add.
* The user can add instructions and ingredients by clicking on the add icon and can delete ingredients and instructions
by clicking on the clear icon.
* The user has the ingredient and instruction fields preserved through sessionStorage. (Note: this feature needs to be 
modified by allowing the user to save his progress, so the form values are saved as well).
* Whenever a user clicks on the reset progress button, a modal pops up asking for confirmation (if the user clicks on the reset
progress button, the form is cleared, if the user clicks on the continue button, she/he can proceed to add her/his recipe).
* A recipe needs to have at least one instruction and at least one ingredient, so when a user clicks on the first ingredient or 
the first instruction an alert is shown at the top of the page.
* It's constructed following a defensive design, each of the fields in the add recipe form will produce an error if the required 
checks are not met (the recipe name needs to have at least 6 characters, an ingredient must have at least 3 characters, an
instruction must have at least 4 characters, all the form fields are required).
* When the user clicks on the add recipe button, the recipe is added in the user recipes collection and the user is redirected to
his/her profile, where he/she can see the recipe.
10. [Edit Recipe Page](/templates/edit_recipe.html)
* It's constructed following a defensive design, each of the fields in the edit recipe form will produce an error if the required 
checks are not met(the recipe name needs to have at least 6 characters, an ingredient must have at least 3 characters, an
instruction must have at least 4 characters, all the form fields are required).
* A recipe needs to have at least one instruction and at least one ingredient, so when a user clicks on the first ingredient or 
the first instruction an alert is shown at the top of the page.
* When a user clicks on the cancel button, he/she is redirected to the view for that recipe (The redirect could have been to the
previous page, but this allows the user to find out that his/her modifications were recorded to the database).
* The user has the ingredient and instruction fields preserved through sessionStorage. (Note: for the edit recipe form, the inputs
are not preserved when he/she leaves the edit page. An extra feature could be added so each user could save his/her edit progress).
11. [Error 404 Page](/templates/error404.html)
* Comprises a custom page not found error.
12. [Error 405 Page](/templates/error405.html)
* Comprises a custom method not allowed error.
13. [Error 500 Page](/templates/error500.html)
* Comprises a custom server error.
14. [Base Template](/templates/base.html)
* Includes all the scripts and css files that have been used for the construction of the other templates.
(Note: 6 additional helper templates have been used for creating the cancel and delete modals, navbar, as well as
inline errors and alerts. They can be found [here](/templates/includes)).
15. Additional Notes
* When clicking logout, the user is automatically removed from the session.
* Added longer set timeout for alerts for improved user experience.
* Paranoid was added to automatically log out the user on a different device. (See notes in 
[app.py](../master/app.py))
* Added SSL certificates and Flask-SSLify that turned out to be no longer needed, but the packages
and imports were kept in case of further uses.
* Added timeout after an hour for a logged in user.


### Features Left To Implement

1. A thing can be added to the website is a functionality for saving progress when the user tries to add a recipe.
2. Another functionality that can be implemented is to allow the admin to approve user recipes in order to add them
to the database recipes.
3. Website design can be improved and CSS fixes can also be made.(It's admittable that the website creator is not particularly
good with colurs, design and CSS.)
4. Pages on screen resizing should look much better, but since the project focused more on functionalities, this aspect was
neglected. 
5. The Python code could be better structured with the help of classes.
6. A comments section (that also contains likes and dislikes) can be added to each recipe so users can post their opinions.
7. A chat could be added so that users could interact with each other.
8. A remember me functionality can be added for login, as well as reset password.\
Note: the creator of the website is planning to implement all these functionalities in the future.



## Bugs Fixed

* Fixed footer span alignment issues.
* Needed to import create_logger from flask.loggings since app.logger.info was not working and the inline
errors would not display for the form helpers.
* Fixed welcome message and styled login and logout buttons flickering bug by adding a hidden class 
to html and then removing it on load. This was an issue related to the fact that the HTML needed to be hidden
before the random message would actually show up on the page.
* Fixed bug with pagination (pagination buttons added even if the number of results exceeded the total number
of recipes) by checking if the offset + limit is less than the total number of recipes.
* Added fix for footer positioning (in the middle of the page) when searching and filtering recipes by adding a custom
`vh100` class for the footer, setting the min-height to `100vh`.
* Fixed overflow for recipe section.
* Implemented fix for bug with likes/dislikes by adding liked and unliked flags for each recipe, so that users could not like 
or dislike a recipe more than once.
* Fixed bug with edit rating text, which actually needed to be inserted into the database before the user would
click on the rate button.
* Added fix for view recipe bug when the user was not in session.
* Fixed image path bug on profile (caused by `urandom` module) by replacing "/" from the random string with "|".
* Implemented fix for bug with rate text changing for each user after one user already rated a specific recipe.
* Fixed bug for pagination when filtering and searching recipes. This was accomplished with some checks in the
[recipes](/templates/recipes.html)  and [search_recipes](/templates/search_recipes.html) and by revising the 
pagination logic in the filter and search routes.
* Fixed bug with local time not being shown, converted date from `datetime.utcnow()` to local string using JavaScript.
* Implemented fix for broken image links by adding a custom image on error for the recipe images and profile image.
* Fixed bug with clear and add icons when removing an ingredient or instruction. Needed to find the parent of the
button when the button was clicked and the parent.parent of the icon when the icon was clicked.
* Added fix for global MySQL cursor not being closed in the profile route.
* Added fix for search results on active filtering by performing debouncing for the AJAX requests. Also aborted the null requests.
* Fixed flash of original content (FOOC) when trying to remove the first ingredient and instruction from the add and edit
recipe forms by disabling the remove button. It is to be agreed that the fix could have been better since the alerts timeout is 
slightly too fast. jQuery could have been used to prevent it, but only vanilla JS was used for the project.
* Fixed delete recipe bug caused by the ID of the recipe.
* Fixed rating bug caused by not initialising the rating of a recipe to 0.
* Fixed bug with cancel update modal not firing up.
* Fixed localStorage bug not being cleared by adding sessionStorage (this was also fixed with the JavaScript utility,
but it turned out that sessionStorage is a much better solution, at least for the scope of this project. It is to be 
mentioned that for the next improvements on the website, localStorage will be used, hence why the utility was not deleted)




## Tech Used

### Front-End Technologies

1. **HTML**, **CSS** and **JavaScript**
    <br>Languages that were used to improve the feel of the Relish website. Pure HTML and CSS was predominantly
    used for designing the recipe views. Note: no jQuery was used for this project because the intention to improve 
    the learning curve with vanilla JavaScript.
2. **Bootstrap v3.3.7**(https://getbootstrap.com/docs/3.3/getting-started/#download)
    <br>**Bootstrap** was used to give the project a responsive layout. As previously specified in the
    existing featured and functionalities section, the original intention was to not use 
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

1. Code was written and tested using Cloud9 and Cloud9 debugger tools.
2. All HTML and CSS code used on the site has been tested using [The W3 CSS Validation Service](https://jigsaw.w3.org/css-validator/) 
and [The W3 Markup Validation Service](https://validator.w3.org/). There were no CSS errors, the CSS warnings relate to box-shadow, border-radius, transform
and object-fit unknown vendor extensions. There were a number of HTML errors, but most of them were related to unclosed elements due to for loops in Jinja templates.
Some of the errors and warnings have been solved, such as style and script unnecessary type issues or empty form actions and inexistent alt tags for images, 
but most of them could not be fixed because they would have created bugs in the functionality and overall aspect of the project. It's also important to mention the fact that [Tidy](https://github.com/htacg/tidy-html5), 
another HTML validator does not count some of the errors that the W3 does. 
3. All Javascript code on the website has been tested using [JSHint](https://jshint.com/). There were no errors found, the warnings found
state the fact that class, arrow functions and template literals are only available in ES6. There are also warnings about let and const related
to ES6 JavaScript.
4. Site viewed and tested in the following browsers:
<br>    i Google Chrome
<br>    ii Mozilla Firefox
<br>    iii Opera
<br>    iv Internet Explorer
<br>    v Safari
The website has limited support for Internet Explorer and no support for Safari.
5. Postman was used for sending GET and POST requests to the website in order to test it
6. Added automated tests for the register and edit forms, as well as basic tests for GET requests.
It's admittable that the tests performed for the app are not the most extensive tests, but having 
any tests is better than having none at all.



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
[Virtual Environment and Packages](https://docs.python.org/3/tutorial/venv.html).

## Credits

I would like to thank all Code Institute Students for helping me along this project and for providing feedback. Some of those people are JoWings, ShaneMuirhead, 
JohnL3, robinz, Sean, Kevin Stewart and Sammy Dartnall, who found quite a lot of bugs in my project. Special thanks goes to my mentor Moosa Hassan for his amazing support
and guidance and to Miro_lead for the sessions that we had each Sunday covering different development topics and for his constructive criticism and feedback. I would also like
to thank [Graffino](https://graffino.com)(Sibiu) for offering me an internship during the time I was doing the project. The internship really helped me improve my UI speed and design skills.
I also learnt a few tricks from them such as [CSS BEM](http://getbem.com/introduction/). Even though the project does not follow the BEM standards, some of the naming 
conventions used in the project are derived from BEM.

### Media

The `images` used on this site were obtained from [Google Images](https://images.google.com/).

### Information

The information used to create this site was from [Allrecipes | Food, friends, and recipe inspiration](https://www.allrecipes.com).
