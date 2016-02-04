from app import db
from flask.ext.bcrypt import generate_password_hash

class Users(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    email = db.Column(db.String(128),unique=True)
    passw = db.Column(db.String(128))
    friends = db.relationship('Friends',backref='user',lazy='dynamic') #relationship -> hakee userille kuuluvat friends -objektit automaattisesti.
    
    """Define the class constructor"""
    def __init__(self,email,passw):
        self.email = email
        self.passw = generate_password_hash(passw)
    #def __str__(self):  #Tämä tulostetaan (esim. print(user[0])), jos määritetty
        #return self.email + ' ' + self.passw + ' ' + str(self.id)
        
class Friends(db.Model):
    id = db.Column(db.Integer, primary_key= True)
    name = db.Column(db.String)
    address = db.Column(db.String)
    age = db.Column(db.Integer)
    filename = db.Column(db.String,default='/static/images/Koala.jpg')
    user_id = db.Column(db.Integer,db.ForeignKey('users.id')) #user_id:llä on relaatio user -taulun id -kenttään (user.id)
    
    """Friends constructor"""
    def __init__(self,name,address,age,user_id):
        self.name = name
        self.address = address
        self.age = age
        self.user_id = user_id
    def __str__(self):  #Tämä tulostetaan, jos määritetty
        text = "This is friends object"
        return text