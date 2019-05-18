import os

# Create a secret key
os.environ["SECRET_KEY"] = "3markHero"
# Storing the MONGO_URI environment variable
os.environ["MONGO_URI"] = "mongodb://admin_recipe:3markHero@ds145923.mlab.com:45923/recipes"
os.environ["MONGO_DBNAME"] = "recipes"
# Storing MySQL connection details in an environment variable
os.environ["DB_USERNAME"] = 'vpsf8o0ljbuwnws9'
os.environ["DB_HOST"] = 'dz8959rne9lumkkw.chr7pe7iynqr.eu-west-1.rds.amazonaws.com'
os.environ["DB_PASS"] =  'lqdqx2ayu621x9d9'
os.environ["DB_NAME"] = 'k4c5aevnff06iuzj'