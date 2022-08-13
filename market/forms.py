from ast import Pass
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField


class RegisterForm(FlaskForm):
    username = StringField(label='Username')
    email = StringField(label='Email')
    password1 = PasswordField("Password")
    password2 = PasswordField("Repeat your password")
    submit = SubmitField(label="Submit")
    