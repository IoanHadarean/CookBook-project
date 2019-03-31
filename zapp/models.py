import os
from flask_pymongo import PyMongo, pymongo
from flask import Flask

app = Flask(__name__)

#Connect to MongoDB database

app.config["MONGO_DBNAME"] = "recipes"
app.config["MONGO_URI"] = "mongodb://me:1403Goagl@ds145923.mlab.com:45923/recipes"

mongo = PyMongo(app)


recipes_collection = mongo.db.recipes.find()
ratings_collection = mongo.db.ratings.find()


""" Find ingredients by cuisine """

# def count_ingredients():
#     count_sugar = 0
#     count_milk = 0
#     count_egg = 0
#     count_flour = 0
#     count_salt = 0
#     count_water = 0
#     count_garlic = 0
#     count_vanilla = 0
#     count_butter = 0
#     count_cuisine = 0
#     for recipe in recipes_collection:
#         if recipe["cuisine_name"] == "Italian": # Change the name of the cuisine to look for other cuisines
#             count_cuisine = count_cuisine + 1
#             print(count_cuisine)
#             items = []
#             for ingredient in recipe["ingredients"]:
#                 itemSplit = ingredient.split(",")
#                 itemSplitAtSpace = itemSplit[0].split(" ")
#                 items.append(itemSplitAtSpace)
#             # print(items)
#                 mergedItems = []
#                 removedDuplicates = []
#                 for item in items:
#                     mergedItems += item
#                     for mergedItem in mergedItems:
#                         if mergedItem not in removedDuplicates:
#                             removedDuplicates.append(mergedItem)
#             # print(mergedItems)
#             print(removedDuplicates)
#             """ Print the count for each ingredient based on the cuisine selected """
#             if "milk" in removedDuplicates: 
#                 count_milk += 1
#             else:
#                 count_milk += 0
#             print(count_milk)
#             if ("egg" in removedDuplicates) | ("eggs" in removedDuplicates):
#                 count_egg += 1
#             else:
#                 count_egg += 0
#             print(count_egg)
#             if "sugar" in removedDuplicates:
#                 count_sugar += 1
#             else:
#                 count_sugar += 0
#             print(count_sugar)
#             if "flour" in removedDuplicates:
#                 count_flour += 1
#             else:
#                 count_flour += 0
#             print(count_flour)
#             if "salt" in removedDuplicates:
#                 count_salt += 1
#             else:
#                 count_salt += 0
#             print(count_salt)
#             if "water" in removedDuplicates:
#                 count_water += 1
#             else:
#                 count_water += 0
#             print(count_water)
#             if "garlic" in removedDuplicates:
#                 count_garlic += 1
#             else:
#                 count_garlic += 0
#             print(count_garlic)
#             if "vanilla" in removedDuplicates:
#                 count_vanilla += 1
#             else:
#                 count_vanilla += 0
#             print(count_vanilla)
#             if "butter" in removedDuplicates:
#                 count_butter += 1
#             else:
#                 count_butter += 0
#             print(count_butter)
# count_ingredients()

""" Percentage of allergens (from all recipes) """
    
# allergens = []
# def percent_allergens():
#     count_recipes = 0
#     count_none = 0
#     count_egg_allergen = 0
#     count_garlic_allergen = 0
#     count_nuts_allergen = 0
#     count_milk_allergen = 0
#     for recipe in recipes_collection:
#         count_recipes += 1
#         # print(count_recipes)
#         if recipe.get('allergen_name') == None:
#             count_none += 1
#             # print(count_none)
#         else:
#             allergens.append(recipe["allergen_name"])
#     # print(allergens)
#     mergedAllergens = []
#     for allergen in allergens:
#         allergenSplit = allergen.split(" ")
#         # print(allergenSplit)
#         mergedAllergens.append(allergenSplit)
#     # print(mergedAllergens)
#     splitAllergens = []
#     for item in mergedAllergens:
#         splitAllergens += item
#     print(splitAllergens)
#     for word in splitAllergens:
#         if word == "egg":
#             count_egg_allergen += 1
#             # print(count_egg_allergen)
#         elif word == "garlic":
#             count_garlic_allergen += 1
#             print(count_garlic_allergen)
#         elif word == "nuts":
#             count_nuts_allergen += 1
#             # print(count_nuts_allergen)
#         elif word == "milk":
#             count_milk_allergen += 1
#             # print(count_milk_allergen)
#     percent_egg = (count_egg_allergen / count_recipes) * 100
#     print(percent_egg)
#     percent_milk = (count_milk_allergen / count_recipes) * 100
#     print(percent_milk)
#     percent_nuts = (count_nuts_allergen / count_recipes) * 100
#     print(percent_nuts)
#     percent_garlic = (count_garlic_allergen / count_recipes) * 100
#     print(percent_garlic)
#     percent_no_allergens = (count_none / count_recipes) * 100
#     print(percent_no_allergens)
            
# percent_allergens()


""" Average calories by cuisine """


# def average_calories():
#     calories_total = 0
#     count_recipes_by_cuisine = 0
#     for recipe in recipes_collection:
#         """ Change the name of cuisine to search for calories by another cuisine
#             (Note: comment this out to calculate average calories for all recipes) """
#         if recipe["cuisine_name"] == "Irish":
#             count_recipes_by_cuisine += 1
#             wordSplit = recipe["calories"].split(" ")
#             # print(wordSplit)
#             calories = int(wordSplit[0])
#             calories_total += calories
#             # print(calories_total)
#             average_calories = calories_total / count_recipes_by_cuisine
#     print(average_calories)
            
# average_calories()


# user_id = 1
# recipe_id = 1
for rating in ratings_collection:
    if rating["user_id"] == 78 and rating["recipe_id"] == "1":
        print(rating["rating"])
        


        
      

    
