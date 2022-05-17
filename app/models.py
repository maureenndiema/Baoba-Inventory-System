from datetime import date
from . import db, Loginmanager
from flask_login import UserMixin
from werkzeug.security import generate_password_hash,check_password_hash
from datetime import datetime

class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255), nullable=False, unique=True)
    email = db.Column(db.String(255), nullable=False, unique=True)
    password_hash = db.Column(db.String(255), nullable=False)  
    profile_pic_path = db.Column(db.String) 

    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')
    
    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)
        
    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    
    def __repr__(self):
        return f'User {self.username}'

class Products(db.Model):
    __tablename__ = 'products'
    id = db.Column(db.Integer, primary_key = True)
    name=db.Column(db.String(90))
    quantity=db.Column(db.Integer ())
    price=db.Column(db.Integer())



    def __repr__(self):
        return f"Products {self.title}"

class Supplier(db.Model):
    __tablename__ = 'supplier'
    id = db.Column(db.Integer, primary_key = True)
    name=db.Column(db.String(90))
    payment_mode=db.Column(db.Integer())

class Category(db.Model):
    __tablename__ = 'category'
    id = db.Column(db.Integer, primary_key = True)
    name=db.Column(db.String(90))

class Orders(db.Model):
    __tablename__ = 'orders'
    id = db.Column(db.Integer, primary_key = True)
    name=db.Column(db.String(90))
    order_date=db.Column(db.DateTime,default = datetime.utcnow)
    amount=db.Column(db.Integer())

class Customer(db.Model):
    __tablename__ = 'customer'
    id = db.Column(db.Integer, primary_key = True)
    name=db.Column(db.String(90))
    email=db.Column(db.String(90))





    
    
    











