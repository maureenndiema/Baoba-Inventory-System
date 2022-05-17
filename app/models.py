from datetime import date
from unicodedata import category
from . import db
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
    Supplier = db.relationship('Supplier', backref='products', lazy='dynamic')
    Category=db.relationship('Category', backref='products', lazy='dynamic')
    Category_id = db.Column(db.Integer, db.ForeignKey('category.id'))
    quantity=db.Column(db.Integer ())
    price=db.Column(db.Integer())



    def __repr__(self):
        return f"Products {self.title}"

class Supplier(db.Model):
    __tablename__ = 'supplier'
    id = db.Column(db.Integer, primary_key = True)
    name=db.Column(db.String(90))
    Products = db.relationship('Product', backref='supplier', lazy='dynamic')
    Category = db.relationship('Category', backref='supplier', lazy='dynamic')
    payment_mode=db.Column(db.Integer())

class Category(db.Model):
    __tablename__ = 'category'
    id = db.Column(db.Integer, primary_key = True)
    name=db.Column(db.String(90))
    Products = db.relationship('Product', backref='category', lazy='dynamic')

class Orders(db.Model):
    __tablename__ = 'orders'
    id = db.Column(db.Integer, primary_key = True)
    name=db.Column(db.String(90))
    Customer = db.relationship('Customer', backref='orders', lazy='dynamic')
    Products = db.relationship('Product', backref='orders', lazy='dynamic')
    order_date=db.Column(db.DateTime,default = datetime.utcnow)
    amount=db.Column(db.Integer())

class Customer(db.Model):
    __tablename__ = 'customer'
    id = db.Column(db.Integer, primary_key = True)
    name=db.Column(db.String(90))
    email=db.Column(db.String(90))
    Orders = db.relationship('Orders', backref='customer', lazy='dynamic')





    
    
    











