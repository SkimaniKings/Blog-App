from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField
from wtforms.validators import DataRequired,Length,Email
class RegistrationForm(FlaskForm):
    Username = StringField('Username' ,validators=[DataRequired(),Length(min=2,max = 20)])
    Email = StringField('Email',validators=[DataRequired(), Email()]) 
    