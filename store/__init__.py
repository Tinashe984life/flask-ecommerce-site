from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://iznbjcptcxrtje:d72e2e6a88737fbe67292926dc13f3f815218c761b2c237981a54a686f083ef4@ec2-54-211-255-161.compute-1.amazonaws.com:5432/d618bte7e6fbug'
app.config['SECRET_KEY'] = 'supersecret'

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'


from store import routes