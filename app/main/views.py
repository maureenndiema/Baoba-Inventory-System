from flask import render_template,request, redirect, url_for, flash
from . import main
from flask_login import login_required
from ..models import *
from .forms import *
from flask_sqlalchemy import SQLAlchemy


#This is the index route where we are going to
#query on all our customer data
@main.route('/')
@main.route('/index')
def index():
    
    return render_template("index.html")

@main.route('/customer')
def customer():
    all_data = Customer.query.all()
    
    return render_template("customer.html", customer = all_data)

#this route is for inserting data to mysql database via html forms
@main.route('/insert', methods = ['POST'])
def insert():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        
        my_data = Customer(name, email)
        db.session.add(my_data)
        db.session.commit()

        flash("Customer Inserted Successfully")

        return redirect(url_for('main.customer'))
        
#this is our update route where we are going to update our customer
@main.route('/update', methods = ['GET', 'POST'])
def update():

    if request.method == 'POST':
        my_data = Customer.query.get(request.form.get('id'))

        my_data.name = request.form['name']
        my_data.email = request.form['email']

        db.session.commit()
        flash("Customer Updated Successfully")

        return redirect(url_for('main.customer'))

#This route is for deleting our customer
@main.route('/delete/<id>/', methods = ['GET', 'POST'])
def delete(id):
    my_data = Customer.query.get(id)
    db.session.delete(my_data)
    db.session.commit()
    flash("Employee Deleted Successfully")

    return redirect(url_for('main.customer'))

#product
@main.route('/product')
def product():
    all_data = Product.query.all()
    
    return render_template("product.html", product = all_data)
#this route is for inserting data to mysql database via html forms
@main.route('/insertproduct', methods = ['POST'])
def insertproduct():
    if request.method == 'POST':
        name = request.form['name']
        quantity = request.form['quantity']
        price = request.form['price']
        # category_id = request.form['category_id']
        # supplier_id = request.form['supplier_id']
        
        my_data = Product(name,quantity,price )
        db.session.add(my_data)
        db.session.commit()

        flash("Product Inserted Successfully")

        return redirect(url_for('main.product'))
        
#this is our update route where we are going to update our customer
@main.route('/updateproduct', methods = ['GET', 'POST'])
def updateproduct():

    if request.method == 'POST':
        my_data = Product.query.get(request.form.get('id'))

        my_data.name = request.form['name']
        my_data.quantity = request.form['quantity']
        my_data.price = request.form['price']
        # my_data.category_id = request.form['category_id']
        # my_data.supplier_id = request.form['supplier_id']
        

        db.session.commit()
        flash("Product Updated Successfully")

        return redirect(url_for('main.product'))

#This route is for deleting our product
@main.route('/deleteproduct/<id>/', methods = ['GET', 'POST'])
def deleteproduct(id):
    my_data = Product.query.get(id)
    db.session.delete(my_data)
    db.session.commit()
    flash("Product Deleted Successfully")

    return redirect(url_for('main.product'))
