import os

# Create a random secret key
secret = "HadareanIoan1403Goagl"
# Storing the MONGO_URI environment variable
os.environ["MONGO_URI"] = "mongodb://me:1403Goagl@ds145923.mlab.com:45923/recipes"
os.environ["MONGO_DBNAME"] = "recipes"
os.environ["SECRET_KEY"] = secret
# Storing MySQL connection details in an environment variable
os.environ["DB_USERNAME"] = 'ioan1997'
os.environ["DB_HOST"] = "localhost"
os.environ["DB_PASS"] =  ''
os.environ["DB_NAME"] = 'flaskapp'