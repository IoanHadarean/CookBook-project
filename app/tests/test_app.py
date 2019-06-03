import unittest
import inspect
import requests
import urllib
import json
from werkzeug.datastructures import ImmutableMultiDict
from unittest.mock import patch
from app import app
from app.models.forms import RegisterForm, EditForm
from flask import request
from bson.objectid import ObjectId

""" Test App Class for unitesting """


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

    """ Test the registration form for errors """
    def test_registerErrors(self):
        for self.item in self.registerForms:
            for key, dictionary in self.item.items():
                if key == 'registerForm1':
                    assert isinstance(dictionary, object)
                    for k, v in vars(dictionary).items():
                        if k == '_errors':
                            self.assertEqual(v, None)

    """ Test the registration form name """
    def test_registerName(self):
        for self.item in self.registerForms:
            for key, dictionary in self.item.items():
                if key == 'registerForm1':
                    assert isinstance(dictionary, object)
                    for k, v in vars(dictionary).items():
                        if k == 'name':
                            for attr, value in vars(v).items():
                                if attr == 'data':
                                    self.assertEqual(value, 'John Doe')
                                    self.assertNotEqual(value, 'J1995Doe')

    """ Test the registration form username """
    def test_registerUsername(self):
        for self.item in self.registerForms:
            for key, dictionary in self.item.items():
                if key == 'registerForm1':
                    assert isinstance(dictionary, object)
                    for k, v in vars(dictionary).items():
                        if k == 'username':
                            for attr, value in vars(v).items():
                                if attr == 'data':
                                    self.assertEqual(value, 'J1995Doe')
                                    self.assertNotEqual(value, 'John Doe')

    """ Test the registration form email """
    def test_registerEmail(self):
        for self.item in self.registerForms:
            for key, dictionary in self.item.items():
                if key == 'registerForm1':
                    assert isinstance(dictionary, object)
                    for k, v in vars(dictionary).items():
                        if k == 'email':
                            for attr, value in vars(v).items():
                                if attr == 'data':
                                    self.assertEqual(value, 'jdoe@yahoo.com')
                                    self.assertNotEqual(value, 'jdoe95@yahoo.com')

    """ Test the registration form password """
    def test_registerPassword(self):
        for self.item in self.registerForms:
            for key, dictionary in self.item.items():
                if key == 'registerForm1':
                    assert isinstance(dictionary, object)
                    for k, v in vars(dictionary).items():
                        if k == 'password':
                            for attr, value in vars(v).items():
                                if attr == 'data':
                                    self.assertEqual(value, 'random')
                                    self.assertNotEqual(value, 'randoms')

    """ Test the registration form confirm password """
    def test_registerConfirmPassword(self):
        for self.item in self.registerForms:
            for key, dictionary in self.item.items():
                if key == 'registerForm1':
                    assert isinstance(dictionary, object)
                    for k, v in vars(dictionary).items():
                        if k == 'confirm':
                            for attr, value in vars(v).items():
                                if attr == 'data':
                                    self.assertEqual(value, 'random')
                                    self.assertNotEqual(value, 'randoms')

    """ Test the edit form for errors """
    def test_updateErrors(self):
        for self.item in self.updateForms:
            for key, dictionary in self.item.items():
                if key == 'updateForm1':
                    assert isinstance(dictionary, object)
                    for k, v in vars(dictionary).items():
                        if k == '_errors':
                            self.assertEqual(v, None)

    """ Test the edit form name """
    def test_updateName(self):
        for self.item in self.updateForms:
            for key, dictionary in self.item.items():
                if key == 'updateForm1':
                    assert isinstance(dictionary, object)
                    for k, v in vars(dictionary).items():
                        if k == 'name':
                            for attr, value in vars(v).items():
                                if attr == 'data':
                                    self.assertEqual(value, 'John Doe')
                                    self.assertNotEqual(value, 'Johnny Doe')

    """ Test the edit form about me field """
    def test_updateAboutMe(self):
        for self.item in self.updateForms:
            for key, dictionary in self.item.items():
                if key == 'updateForm1':
                    assert isinstance(dictionary, object)
                    for k, v in vars(dictionary).items():
                        if k == 'about_me':
                            for attr, value in vars(v).items():
                                if attr == 'data':
                                    self.assertEqual(value, 'I am John')
                                    self.assertNotEqual(value, 'I am Ioan')

    """ Test the edit form email """
    def test_updateEmail(self):
        for self.item in self.updateForms:
            for key, dictionary in self.item.items():
                if key == 'updateForm1':
                    assert isinstance(dictionary, object)
                    for k, v in vars(dictionary).items():
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
    def test_get_recipe(self):
        url = 'https://relish-cookbook.herokuapp.com/get_recipe/5c7ad43efb6fc072012c862f'
        response = requests.get(url)
        if response.ok:
            return response.text
        else:
            return 'Bad Response'

    """ Test get request for get_user_recipe route """
    def test_get_user_recipe(self):
        url = 'https://relish-cookbook.herokuapp.com/get_user_recipe/12483f483c543a857e352'
        response = requests.get(url)
        if response.ok:
            return response.text
        else:
            return 'Bad Response'

    """ Test get request for profile route """
    def test_profile(self):
        url = 'https://relish-cookbook.herokuapp.com/profile'
        response = requests.get(url)
        if response.ok:
            return response.text
        else:
            return 'Bad Response'

    """ Test get request for index route """
    def test_index(self):
        url = 'https://datacentricmilestoneproject-ioan1997.c9users.io:8080/recipes?pagination_offset=0&pagination_limit=6'
        response = requests.get(url)
        if response.ok:
            return response.text
        else:
            return 'Bad Response'
