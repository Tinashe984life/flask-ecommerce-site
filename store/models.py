from datetime import datetime
from store import db, login_manager
from flask_login import UserMixin
#from sqlalchemy_utils import ScalarListTypes

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    surname = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(50), unique=True,nullable=False)
    cellphone = db.Column(db.String(20), nullable=False)
    password = db.Column(db.String(60), nullable=False)
    products = db.relationship('Cart', backref='user')
    checks = db.relationship('Orders', backref='user')

    def __repr__(self):
        return f"User('{self.name}','{self.surname}', '{self.email}')"


class Cart(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable=False)
    description = db.Column(db.String(250), nullable=False)
    price = db.Column(db.Integer, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return f"Cart('{self.name}', '{self.description}', '{self.price}')"


class Orders(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    items = db.Column(db.String, nullable=False)
    order_total = db.Column(db.Integer, nullable=False)
    owner_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return f"Orders('{self.date_created}', '{self.items}', '{self.order_total}')"