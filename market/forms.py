from ast import Pass
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import Length, EqualTo, Email, DataRequired,ValidationError
from market.models import User

class RegisterForm(FlaskForm):
    username = StringField(label='Username', validators=[
                           Length(min=2, max=30), DataRequired()])
    email = StringField(label='Email', validators=[Email(), DataRequired()])
    password1 = PasswordField("Password", validators=[
                              Length(min=6), DataRequired()])
    password2 = PasswordField("Repeat your password",
                              validators=[EqualTo("password1",message="Repeat password must be equal to password."), DataRequired()])
    submit = SubmitField(label="Create Account")

    def validate_username(self,username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError("Username already exists! Please try a diffrent username .")

    def validate_email(self,email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError("Email already exists! Please try a diffrent email .")

class LoginForm(FlaskForm):
    username = StringField(label="User Name",validators=[DataRequired()])
    password = PasswordField(label="Password",validators=[DataRequired()])
    submit = SubmitField(label="Sign in")

class PurchaseForm(FlaskForm):
    submit = SubmitField(label="Purchase this item")

class SellForm(FlaskForm):
    submit = SubmitField(label="Sell this item")