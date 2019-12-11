from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
app = Flask(__name__)
app.config['SECRET_KEY'] = '49eb64b6fd097dc25da244cff0c7f062'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager=LoginManager(app)
login_manager.login_view='login'
login_manager.login_message_category='info'
from fyp import routes