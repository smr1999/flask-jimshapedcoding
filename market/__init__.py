from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///market.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = '74255dbc4a797485edfba9f74b751e40'

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login = LoginManager(app)
login.login_view = "login_page"
login.login_message_category = "info"

from market import routes,models