import os
from flask import Flask, redirect, render_template, request, url_for, flash, session
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)
app.secret_key = os.getenv("SECRET", "1403goagl")
app.config["MONGO_DBNAME"] = "recipes"
app.config["MONGO_URI"] = "mongodb://goagl:3markHero@ds145923.mlab.com:45923/recipes"

mongo = PyMongo(app)

@app.route('/', methods = ["GET", "POST"])
def index():
    """Main page with instructions"""
    
    if request.method == "POST":
        session["username"] = request.form["username"]
        
    if "username" in session:
        return redirect(url_for("user", username = session["username"]))
        
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host=os.environ.get('IP'),
        port=int(os.environ.get('PORT')),
        debug=True)