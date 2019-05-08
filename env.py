import os

# Create a secret key
os.environ["SECRET_KEY"] = "HadareanIoan1403Goagl"
# Storing the MONGO_URI environment variable
os.environ["MONGO_URI"] = "mongodb://me:1403Goagl@ds145923.mlab.com:45923/recipes"
os.environ["MONGO_DBNAME"] = "recipes"
# Storing MySQL connection details in an environment variable
os.environ["DB_USERNAME"] = 'bd5b3ae81fbd76'
os.environ["DB_HOST"] = 'eu-cdbr-west-02.cleardb.net'
os.environ["DB_PASS"] =  '6c517b98'
os.environ["DB_NAME"] = 'heroku_9f1934449cd3875'