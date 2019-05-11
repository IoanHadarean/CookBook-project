import unittest, inspect
from werkzeug.datastructures import ImmutableMultiDict
import app, re
from app import RegisterForm, EditForm

class TestApp(unittest.TestCase):
    def test_registerForm(self):
        registerForm = RegisterForm(ImmutableMultiDict([('confirm', 'random'), ('username', 'J1995Doe'), ('password', 'random'), ('name', 'John Doe'), ('email', 'jdoe@yahoo.com')]))
        assert isinstance(registerForm, object)
        for k, v in vars(registerForm).items():
            if (k == '_fields'):
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
            if k == 'username':
                for attr, value in vars(v).items():
                    if attr == 'data':
                        self.assertEqual(value, 'J1995Doe')
            if k == 'email':
                for attr, value in vars(v).items():
                    if attr == 'data':
                        self.assertEqual(value, 'jdoe@yahoo.com')
            if k== 'confirm':
                for attr, value in vars(v).items():
                    if attr == 'data':
                        self.assertEqual(value, 'random')
            if k== 'password':
                for attr, value in vars(v).items():
                    if attr == 'data':
                        self.assertEqual(value, 'random')
    def test_editForm(self):
        editForm = EditForm(ImmutableMultiDict([('about_me', 'I am Ioan'), ('name', 'Ioan'), ('email', 'ioan@yahoo.com')]))
        assert isinstance(editForm, object)
        for k, v in vars(editForm).items():
            if (k == '_fields'):
                for attr, value in vars(v).items():
                    if attr == '_OrderedDict__map':
                        for i in value.values():
                            assert isinstance(i, object)
            if k == '_errors':
                self.assertEqual(v, None)
            if k == 'name':
                for attr, value in vars(v).items():
                    if attr == 'data':
                        self.assertEqual(value, 'Ioan')
            if k == 'about_me':
                for attr, value in vars(v).items():
                    if attr == 'data':
                        self.assertEqual(value, 'I am Ioan')
    def test_profileImage(self):
        profileImage = EditForm(ImmutableMultiDict([('picture', 'Group 6.png')]))
        assert isinstance(profileImage, object)
        for k, v in vars(profileImage).items():
            if (k == '_fields'):
                for attr, value in vars(v).items():
                    if attr == '_OrderedDict__map':
                        for i, j in value.items():
                            if i == 'picture':
                                assert isinstance(j, object)
                                self.assertEqual(inspect.getmembers(j, predicate=inspect.ismethod), [])
                            