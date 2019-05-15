import unittest
import inspect
import requests
import urllib
import json
from werkzeug.datastructures import ImmutableMultiDict
import app
from unittest.mock import patch
from app import RegisterForm, EditForm, filter_results
from flask import request
from bson.objectid import ObjectId

""" Test App Class  for unitesting """


class TestApp(unittest.TestCase):
    """ Set up the forms for testing """
    def setUp(self):
        # Create form lists
        self.profileImages = []
        self.registerForms = []
        self.updateForms = []
        # Create form objects
        self.registerForm1 = RegisterForm(ImmutableMultiDict([('confirm', 'random'), ('username', 'J1995Doe'), ('password', 'random'), ('name', 'John Doe'), ('email', 'jdoe@yahoo.com')]))
        self.registerForm2 = RegisterForm(ImmutableMultiDict([('confirm', 'password'), ('username', 'Ana1532'), ('password', 'random'), ('name', 'Ana Brooklyn'), ('email', 'anabrook89@yahoo.com')]))
        self.updateForm1 = EditForm(ImmutableMultiDict([('about_me', 'I am John'), ('name', 'John Doe'), ('email', 'jdoe95@yahoo.com')]))
        self.updateForm2 = EditForm(ImmutableMultiDict([('about_me', 'I am Ana'), ('name', 'Ana Brooklyn'), ('email', 'anabrook1489@yahoo.com')]))
        self.profileImage1 = EditForm(ImmutableMultiDict([('picture', 'Group 6.png')]))
        self.profileImage2 = EditForm(ImmutableMultiDict([('picture', 'avatar.png')]))

        # Append objects to form lists
        self.profileImages.append({'profileImage1': self.profileImage1})
        self.profileImages.append({'profileImage2': self.profileImage2})
        self.registerForms.append({'registerForm1': self.registerForm1})
        self.registerForms.append({'registerForm2': self.registerForm2})
        self.updateForms.append({'updateForm1': self.updateForm1})
        self.updateForms.append({'updateForm2': self.updateForm2})
    """ Additional function to run after tests have been finished """
    def tearDown(self):
        pass
    """" Test the registration form values """
    def test_registerForms(self):
        for self.item in self.registerForms:
            for key, dictionary in self.item.items():
                if key == 'registerForm1':
                    assert isinstance(dictionary, object)
                    for k, v in vars(dictionary).items():
                        if k == '_fields':
                            for attr, value in vars(v).items():
                                if attr == '_OrderedDict__map':
                                    for i in value.values():
                                        assert isinstance(i, object)
                        if k == '_errors':
                            self.assertEqual(v, None)
                        if k == 'name':
                            for attr, value in vars(v).items():
                                if attr == 'data':
                                    self.assertEqual(value, 'John Doe')
                                    self.assertNotEqual(value, 'J1995Doe')
                        if k == 'username':
                            for attr, value in vars(v).items():
                                if attr == 'data':
                                    self.assertEqual(value, 'J1995Doe')
                                    self.assertNotEqual(value, 'John Doe')
                        if k == 'email':
                            for attr, value in vars(v).items():
                                if attr == 'data':
                                    self.assertEqual(value, 'jdoe@yahoo.com')
                                    self.assertNotEqual(value, 'jdoe95@yahoo.com')
                        if k == 'confirm':
                            for attr, value in vars(v).items():
                                if attr == 'data':
                                    self.assertEqual(value, 'random')
                                    self.assertNotEqual(value, 'randoms')
                        if k == 'password':
                            for attr, value in vars(v).items():
                                if attr == 'data':
                                    self.assertEqual(value, 'random')
                                    self.assertNotEqual(value, 'randoms')
    """ Test the edit form values """           
    def test_updateForm(self):
        for self.item in self.updateForms:
            for key, dictionary in self.item.items():
                if key == 'updateForm1':
                    assert isinstance(dictionary, object)
                    for k, v in vars(dictionary).items():
                        if k == '_fields':
                            for attr, value in vars(v).items():
                                if attr == '_OrderedDict__map':
                                    for i in value.values():
                                        assert isinstance(i, object)
                        if k == '_errors':
                            self.assertEqual(v, None)
                        if k == 'name':
                            for attr, value in vars(v).items():
                                if attr == 'data':
                                    self.assertEqual(value, 'John Doe')
                                    self.assertNotEqual(value, 'Johnny Doe')
                        if k == 'about_me':
                            for attr, value in vars(v).items():
                                if attr == 'data':
                                    self.assertEqual(value, 'I am John')
                                    self.assertNotEqual(value, 'I am Ioan')
                        if k == 'email':
                            for attr, value in vars(v).items():
                                if attr == 'data':
                                    self.assertEqual(value, 'jdoe95@yahoo.com')
                                    self.assertNotEqual(value, 'jdoe@yahoo.com')
    """ Test profile image from edit form """                   
    def test_profileImage(self):
        for self.item in self.profileImages:
            for key, dictionary in self.item.items():
                if key == 'profileImage1':
                    assert isinstance(dictionary, object)
                    for k, v in vars(dictionary).items():
                        if (k == '_fields'):
                            for attr, value in vars(v).items():
                                if attr == '_OrderedDict__map':
                                    for i, j in value.items():
                                        if i == 'picture':
                                            assert isinstance(j, object)
                                            self.assertEqual(inspect.getmembers(j, predicate=inspect.ismethod), [])
    """ Test get request for get_recipe route """
    def test_getRecipe(self):
        url = 'https://relish-cookbook.herokuapp.com/get_recipe/5c7ad43efb6fc072012c862f'
        response = requests.get(url)
        if response.ok:
            return response.text
        else:
            return 'Bad Response'
    """ Test get request for get_user_recipe route """    
    def test_getUserRecipe(self):
        url = 'https://relish-cookbook.herokuapp.com/get_user_recipe/12483f483c543a857e352'
        response = requests.get(url)
        if response.ok:
            return response.text
        else:
            return 'Bad Response'
