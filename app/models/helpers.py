import os
import json
from app import env
from flask_pymongo import PyMongo, pymongo
from flask import Flask

app = Flask(__name__)

# Connect to MongoDB database

app.config["MONGO_DBNAME"] = os.getenv("MONGO_DBNAME")
app.config["MONGO_URI"] = os.getenv("MONGO_URI")

mongo = PyMongo(app)

recipes = mongo.db.recipes
recipes_collection = mongo.db.recipes.find()
ratings_collection = mongo.db.ratings.find()


""" Scripts that have been used for the statistics charts
    (Finding out the allergen percentages, ingredients count
    and average calories per cuisine) """


""" Find ingredients by cuisine """


def count_ingredients():
    count_sugar = 0
    count_milk = 0
    count_egg = 0
    count_flour = 0
    count_salt = 0
    count_water = 0
    count_garlic = 0
    count_vanilla = 0
    count_butter = 0
    count_cuisine = 0
    for recipe in recipes_collection:
        # Change the name of the cuisine to look for other cuisines
        if recipe["cuisine_name"] == "Italian":
            count_cuisine = count_cuisine + 1
            items = []
            for ingredient in recipe["ingredients"]:
                itemSplit = ingredient.split(",")
                itemSplitAtSpace = itemSplit[0].split(" ")
                items.append(itemSplitAtSpace)
                mergedItems = []
                removedDuplicates = []
                for item in items:
                    mergedItems += item
                    for mergedItem in mergedItems:
                        if mergedItem not in removedDuplicates:
                            removedDuplicates.append(mergedItem)
            # Print the count for each ingredient based on the cuisine selected
            if "milk" in removedDuplicates:
                count_milk += 1
            else:
                count_milk += 0
            print(count_milk)
            if ("egg" in removedDuplicates) | ("eggs" in removedDuplicates):
                count_egg += 1
            else:
                count_egg += 0
            print(count_egg)
            if "sugar" in removedDuplicates:
                count_sugar += 1
            else:
                count_sugar += 0
            print(count_sugar)
            if "flour" in removedDuplicates:
                count_flour += 1
            else:
                count_flour += 0
            print(count_flour)
            if "salt" in removedDuplicates:
                count_salt += 1
            else:
                count_salt += 0
            print(count_salt)
            if "water" in removedDuplicates:
                count_water += 1
            else:
                count_water += 0
            print(count_water)
            if "garlic" in removedDuplicates:
                count_garlic += 1
            else:
                count_garlic += 0
            print(count_garlic)
            if "vanilla" in removedDuplicates:
                count_vanilla += 1
            else:
                count_vanilla += 0
            print(count_vanilla)
            if "butter" in removedDuplicates:
                count_butter += 1
            else:
                count_butter += 0
            print(count_butter)
# count_ingredients()

""" Percentage of allergens (from all recipes) """


allergens = []


def percent_allergens():
    count_recipes = 0
    count_none = 0
    count_egg_allergen = 0
    count_garlic_allergen = 0
    count_nuts_allergen = 0
    count_milk_allergen = 0
    for recipe in recipes_collection:
        count_recipes += 1
        if recipe.get('allergen_name') is None:
            count_none += 1
        else:
            allergens.append(recipe["allergen_name"])
    mergedAllergens = []
    for allergen in allergens:
        allergenSplit = allergen.split(" ")
        mergedAllergens.append(allergenSplit)
    splitAllergens = []
    for item in mergedAllergens:
        splitAllergens += item
    print(splitAllergens)
    for word in splitAllergens:
        if word == "egg":
            count_egg_allergen += 1
        elif word == "garlic":
            count_garlic_allergen += 1
        elif word == "nuts":
            count_nuts_allergen += 1
        elif word == "milk":
            count_milk_allergen += 1
    percent_egg = (count_egg_allergen / count_recipes) * 100
    print(percent_egg)
    percent_milk = (count_milk_allergen / count_recipes) * 100
    print(percent_milk)
    percent_nuts = (count_nuts_allergen / count_recipes) * 100
    print(percent_nuts)
    percent_garlic = (count_garlic_allergen / count_recipes) * 100
    print(percent_garlic)
    percent_no_allergens = (count_none / count_recipes) * 100
    print(percent_no_allergens)
# percent_allergens()


""" Average calories by cuisine """


def average_calories():
    calories_total = 0
    count_recipes_by_cuisine = 0
    for recipe in recipes_collection:
        """ Change the name of cuisine to search for calories
            by another cuisine (Note: comment this out to calculate
            average calories for all recipes) """
        if recipe["cuisine_name"] == "Irish":
            count_recipes_by_cuisine += 1
            wordSplit = recipe["calories"].split(" ")
            calories = int(wordSplit[0])
            calories_total += calories
            average_calories = calories_total / count_recipes_by_cuisine
    print(average_calories)
# average_calories()


""" Script for dumping recipe ids into a JSON file """

full_recipeIds = []
for recipe in recipes_collection:
    recipeId = str(recipe["_id"])
    full_recipeIds.append(recipeId)

with open("urls.json", 'w') as file:
    json.dump(full_recipeIds, file)


""" Script for updating multiple values in MongoDB collection """

recipes.update({}, {"$set": {"dislikes": 0}}, upsert=False, multi=True)
recipes.update({}, {"$set": {"likes": 0}}, upsert=False, multi=True)
recipes.update({}, {"$set": {"rating": "0"}}, upsert=False, multi=True)

""" Create list of dictionaries from the search form data """
def get_results(data):
    # Create temporary list for filters storage
    filters = list()
    # Loop through each of the keys from the form
    for key in data:
        # Store the original key for later use
        value_key = key
        # Split the key by "-"
        key = key.split("-")
        # Take the first value from the list
        key = key[0]
        # Create temporary dictionary for storing the filter
        search_filter = dict()
        search_filter[key] = data[value_key]
        # Append the filter to the list of filters
        filters.append(search_filter)
    return filters
        