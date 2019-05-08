import os

# Create a secret key
os.environ["SECRET_KEY"] = "HadareanIoan1403Goagl"
# Storing the MONGO_URI environment variable
os.environ["MONGO_URI"] = "mongodb://me:1403Goagl@ds145923.mlab.com:45923/recipes"
os.environ["MONGO_DBNAME"] = "recipes"
# Storing MySQL connection details in an environment variable
os.environ["DB_USERNAME"] = 'b928fe973015c4'
os.environ["DB_HOST"] = 'eu-cdbr-west-02.cleardb.net'
os.environ["DB_PASS"] =  '1948e87'
os.environ["DB_NAME"] = 'heroku_8d9395611c0babe'