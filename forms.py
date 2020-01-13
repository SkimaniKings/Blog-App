from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField
from wtforms.validators import DataRequired,Length,Email,EqualTo
class RegistrationForm(FlaskForm):
    Username = StringField('Username' ,validators=[DataRequired(),Length(min=2,max = 20)])
    Email = StringField('Email',validators=[DataRequired(), Email()]) 
    Password = PasswordField('Password',validators=DataRequired())
    confirm_password = PasswordField('Confirm Password', validators=DataRequired())