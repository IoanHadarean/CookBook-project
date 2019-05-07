import os

# Create a secret key
os.environ["SECRET_KEY"] = "HadareanIoan1403Goagl"
# Storing the MONGO_URI environment variable
os.environ["MONGO_URI"] = "mongodb://me:1403Goagl@ds145923.mlab.com:45923/recipes"
os.environ["MONGO_DBNAME"] = "recipes"
# Storing MySQL connection details in an environment variable
os.environ["DB_USERNAME"] = '$C9_USER'
os.environ["DB_HOST"] = "localhost"
os.environ["DB_PASS"] =  ''
os.environ["DB_NAME"] = 'flaskapp'