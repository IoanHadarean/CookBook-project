import unittest
from werkzeug.datastructures import ImmutableMultiDict
import app, re
from app import RegisterForm

class TestApp(unittest.TestCase):
    def test_registerForm(self):
        registerForm = RegisterForm(ImmutableMultiDict([('confirm', 'random'), ('username', 'J1995Doe'), ('password', 'random'), ('name', 'John Doe'), ('email', 'jdoe@yahoo.com')]))
        assert isinstance(registerForm, object)
        for k, v in vars(registerForm).items():
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