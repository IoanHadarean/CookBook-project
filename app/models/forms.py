from wtforms import Form, StringField, TextAreaField, PasswordField
from wtforms.validators import DataRequired, Length, Email, EqualTo
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms.validators import DataRequired, Length, Email, EqualTo
from wtforms.validators import ValidationError


""" RegisterForm class with fields and validators """


class RegisterForm(Form):
    name = StringField('Name',
                       validators=[DataRequired(), Length(min=6, max=50)])
    username = StringField('Username',
                           validators=[DataRequired(), Length(min=6, max=25)])
    email = StringField('Email',
                        validators=[DataRequired(),
                                    Email(), Length(min=15, max=50)])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm = PasswordField('Confirm Password',
                            validators=[DataRequired(), EqualTo('password',
                                        message='Passwords do not match')])


""" Edit Profile Form class with fields and validators """


class EditForm(Form):
    name = StringField('Name',
                       validators=[DataRequired(), Length(min=6, max=50)])
    email = StringField('Email',
                        validators=[DataRequired(), Email(),
                                    Length(min=11, max=50)])
    about_me = TextAreaField('About Me', validators=[Length(min=12, max=140)])
    picture = FileField('Update Profile Picture',
                        validators=[FileRequired(),
                                    FileAllowed(['jpg', 'jpeg', 'png'])])

