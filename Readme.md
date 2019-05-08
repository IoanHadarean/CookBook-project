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
1. User is able to go to the main page 
2. User is able to navigate to different destinations on the same page
3. User is able to send emails using the contact form
4. User is able to search locations in different countries using the search fieldbox
5. User is able to find touristique attractions, bars, restaurants and accomodation for a dream holiday
6. User is able to get the rating of the searched places and to click on markers to view more details

### Wireframe

<a href="https://imgbb.com/"><img src="https://image.ibb.co/h8dRfA/Bullet-Travel.png" alt="Bullet-Travel" border="0"></a>


### Existing Features

**Single Page Application(SPI) that surprises with the user centric design and visual content**
* Easy-to-use navigation system
* Sticky navbar when scrolling on the page
* Internal links to different sections on the page
* Radio buttons that are used to filter museums, restaurants, bars, hotels, airports and banks
* Logo for travel agency in order to make it unique
* Search location box for entering a location
* Dropdown list with destination countries
* Google Maps
* Autocomplete function for cities (Note: The function eventually autocompletes everything)
* Google Map markers for finding the rating of a certain place, address and more details
* Sections for every destination
* Tariffs for each destination(UK, USA, Romania and Australia)
* Itinerary for every destination
* HD images used for every destination
* Bounce animation effect for each destination header
* Contact form with submit button
* Sending emails function
* Reset form and alert when submitting an email
* Responsive web design
* Grid system 

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
5. Sending emails functionality was tested using Gmail and EmailJS.
6. SendMail function was tested using Jasmine Framework.
7. Postman was used for sending GET and POST requests to the website in order to test it

## Deployment
Note: the coding for the project was done in Cloud9. 
1. Created a new git repository by typing *`git init`* in the terminal.
2. Added the git remote by typing *`git remote add origin https://github.com/IoanHadarean/CookBook-project.git`* in the CLI.
3. Created a requirements.txt file using *`(sudo) pip3 freeze --local > requirements.txt`*. This file was necessary for the deployment process
since it allowed Heroku to figure out what packages should be installed when deploying the app on the production server.
4. Created a Procfile that declared the type of application, in this case a web application. The command used for initialising the Procfile
was *`echo web: python app.py > Procfile`*.
5. Logged in on [Heroku](https://www.heroku.com/home) by typing *`heroku login`* in the terminal. 
6. Pushed the code from git master branch to Heroku by using the following command:
*`git push heroku master`*.
Note: Heroku is a cloud-based platform that makes it easy to deploy and scale Python apps, regardless if the framework used is
Flask or Django.
7. Added the config variables to Heroku in the settings option:
*`CLEARDB-DATABASE-URL`*
*`DBHOST`*
*`DBNAME`*
*`DBPASS`*
*`DBUSERNAME`*
*`IP`*
*`PORT`*
*`SECRET_KEY`*
*`MONGO_URI`*
*`MONGO_DBNAME`*.
8. Exported the local database to Heroku by using the free ClearDB add-on provided by the platform.
9. Dumped all the MYSQL scripts that were used for creating the *`flaskapp`* database locally by running 
*`mysqldump -u $C9_USER -p flaskapp > flaskapp.sql`* in the CLI.
10. Connected to the ClearDB database by typing *`mysql -u username -h cleardbhost -p heroku_9f1934449cd3875`* in the terminal.
11. Ran the scripts from [flaskapp.sql](../master/flaskapp.sql) into MySQL terminal to repopulate the data.



### Getting the code up and running
The project runs on a production server called Heroku. If you want to run the project locally please follow these instructions.
Note the fact that you would need to contact the app administrator in order to get the connection details that were used in the construction
of this app.
1. Download and install Python3 via the Command Line Interface(CLI) (Make sure you are using Python3, the project won't run on Python2). 
2. In order to check the version of Python installed type python --version in the terminal.
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
