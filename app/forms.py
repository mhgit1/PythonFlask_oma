from flask.ext.wtf import Form
from wtforms import StringField,PasswordField,SubmitField,IntegerField
from wtforms.validators import Required,Email,NumberRange

""" Nämä korvattu blueprint\auth\auth_forms.py -tiedostossa
class LoginForm(Form):
    email = StringField('Enter your email',validators=[Required(),Email()])
    passw = PasswordField('Enter password',validators=[Required()])
    submit = SubmitField('Login')
    
class RegisterForm(Form):
    email = StringField('Enter your email',validators=[Required(),Email()])
    passw = PasswordField('Enter password',validators=[Required()])
    submit = SubmitField('Register')
"""

""" Tämä korvattu blueprint\ud\ud_forms.py -tiedostossa
class FriendForm(Form):
    name = StringField('Enter friend´s name',validators=[Required()])
    address = StringField('Enter friend´s address',validators=[Required()])
    age = IntegerField('Enter friend´s age',validators=[Required(),NumberRange(min=0,max=120,message="Enter value between 0-120")])
    submit = SubmitField('Save')
"""
