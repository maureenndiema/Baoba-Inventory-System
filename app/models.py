from datetime import date
from unicodedata import category
from . import db
from flask_login import UserMixin
from werkzeug.security import generate_password_hash,check_password_hash
from datetime import datetime
from . import login_manager

# decorator
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

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

class Product(db.Model):
    __tablename__ = 'products'
    id = db.Column(db.Integer, primary_key = True)
    name=db.Column(db.String(90))
    quantity=db.Column(db.Integer ())
    price=db.Column(db.Integer())
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'))
    supplier_id = db.Column(db.Integer, db.ForeignKey('supplier.id'))
    
    

    def __repr__(self):
        return f"Product {self.name}"

class Supplier(db.Model):
    __tablename__ = 'supplier'
    id = db.Column(db.Integer, primary_key = True)
    name=db.Column(db.String(90))
    payment_mode=db.Column(db.Integer())
    product = db.relationship('Product', backref='supplier', lazy='dynamic')
    
    def __repr__(self):
        return f'User {self.name}'
    

class Category(db.Model):
    __tablename__ = 'category'
    id = db.Column(db.Integer, primary_key = True)
    name=db.Column(db.String(90))
    product = db.relationship('Product', backref='category', lazy='dynamic')
    
    def __repr__(self):
        return f'User {self.name}'

class Orders(db.Model):
    __tablename__ = 'orders'
    id = db.Column(db.Integer, primary_key = True)
    order_date=db.Column(db.DateTime,default = datetime.utcnow)
    amount=db.Column(db.Integer())
    customer_id = db.Column(db.Integer, db.ForeignKey('customer.id'))
    
    def __repr__(self):
        return f'User {self.order}'

class Customer(db.Model):
    __tablename__ = 'customer'
    id = db.Column(db.Integer, primary_key = True)
    name=db.Column(db.String(90))
    email=db.Column(db.String(90))
    orders = db.relationship('Orders', backref='customer', lazy='dynamic')
    
    def __init__(self, name, email):

        self.name = name
        self.email = email






    
    
    











