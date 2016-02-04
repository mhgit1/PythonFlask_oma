from flask.ext.wtf import Form
from wtforms import StringField,SubmitField,IntegerField,FileField
from wtforms.validators import Required,Email,NumberRange


class FriendForm(Form):
    name = StringField('Enter friend´s name',validators=[Required()])
    address = StringField('Enter friend´s address',validators=[Required()])
    age = IntegerField('Enter friend´s age',validators=[Required(),NumberRange(min=0,max=120,message="Enter value between 0-120")])
    upload_file = FileField('Upload Image')
    submit = SubmitField('Save')