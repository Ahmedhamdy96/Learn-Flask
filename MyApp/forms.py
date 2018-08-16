# pip install flask-wtf
from flask_wtf import FlaskForm

from wtforms import StringField    # for strings fields
from wtforms import PasswordField  # for passwords fields
from wtforms import SubmitField    # to make submit buttons
from wtforms import BooleanField   # a True or False Field ( for remember me field for example )

from wtforms.validators import DataRequired  # DataRequired() to validate that the field is not empty
from wtforms.validators import Length        # to set the length of the data accepted in the field
from wtforms.validators import Email         # to check its a valid email form
from wtforms.validators import EqualTo       # to be sure that the Data in two fields are identical

#---------------------------------------------------------------------------------------------------------------------------
class RegistrationForm(FlaskForm):
    # Length(min=2 , max=20 ) =>  username length in between 2 and 20 characters
    # DataRequired()          => username can't be empty
    username = StringField('User Name : ' , validators=[ DataRequired() , Length(min=2 , max=20 ) ])
    email = StringField('Email : ' , validators=[DataRequired()  , Email()] )
    password = PasswordField('Password : ' , validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password : ' , validators=[DataRequired() , EqualTo('password')])
    submit = SubmitField('Sign Up')
#-------------------------------------------------------------------------------------------------------------------------------
class LoginForm(FlaskForm):
    email = StringField('Email : ' , validators=[DataRequired() , Email() ])
    password = PasswordField('Password : ' , calidators=[DataRequired()])
    remember = BooleanField('Remember Me : ')
    submit = SubmitField('Login')
