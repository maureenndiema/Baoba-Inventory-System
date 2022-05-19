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
