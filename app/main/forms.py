from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField,TextAreaField
from wtforms.validators import DataRequired, Email, EqualTo,ValidationError
from flask_wtf.file import FileField, FileAllowed
from flask_login import current_user


class CustomerForm(FlaskForm):
    name = TextAreaField('Name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired()])
    submit = SubmitField('Add Customer')