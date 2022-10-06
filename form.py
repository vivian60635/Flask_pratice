from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, BooleanField
from wtforms.validators import DataRequired, Length, EqualTo
from model import UserModel, RoleModel

class EditForm(FlaskForm):
    book_name = StringField('Book Name', validators=[DataRequired(message='Not Null')])
    author = StringField('Author Name', validators=[DataRequired(message='Not Null')])
    add = SubmitField('Add')
    delete = SubmitField('Delete')


class SearchForm(FlaskForm):
    book_name = StringField('Book Name')
    author = StringField('Author Name')
    submit = SubmitField('Submit')
    edit = SubmitField('Edit Book Store')

#  從繼承FlaskForm開始
class RegistrationForm(FlaskForm):

    username = StringField('UserName', validators=[DataRequired(message='Not Null'), Length(min=4, max=25)])
    email = StringField('Email', validators=[DataRequired(message='Not Null'), Length(min=4, max=25)])
    password = PasswordField('New Password')
    confirm = PasswordField('Repeat Password', validators= [DataRequired(), EqualTo('password', message='Passwords must match')])
    accept_tos = BooleanField('I accept the TOS', [DataRequired()])
    submit = SubmitField('Submit')

    def validate_name(self, username):
        if UserModel.query.filter_by(name=username).first():
            raise 'Username already register by somebody'

class LoginForm(FlaskForm):
    username = StringField('UserName')
    password = PasswordField('Password')
    submit = SubmitField('Submit')
    registr = SubmitField('Registr')