import os

# Create a secret key
os.environ["SECRET_KEY"] = "3markHero"
# Storing the MONGO_URI environment variable
os.environ["MONGO_URI"] = "mongodb://admin_recipe:3markHero@ds145923.mlab.com:45923/recipes"
os.environ["MONGO_DBNAME"] = "recipes"
# Storing MySQL connection details in an environment variable
os.environ["DB_USERNAME"] = 'e7uhzupcv0npu7fp'
os.environ["DB_HOST"] = 'wyqk6x041tfxg39e.chr7pe7iynqr.eu-west-1.rds.amazonaws.com'
os.environ["DB_PASS"] =  'v7mib76bqqp4d3yu'
os.environ["DB_NAME"] = 'rg0qy5ylfuoz0084'