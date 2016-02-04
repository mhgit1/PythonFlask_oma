from app import app 
"""Monirivinen kommentti: Ensimmäinen app viittaa app -kansioon 
    ja toinen __init__.py -tiedostossa määritettyyn app -nimeen"""
#Yksirivinen kommentti: importilla voi tuoda toisessa tiedostossa määritettyjä moduuleja

#render_template gives you access to Jinja2 template engine
#request -objektilla saadaan requestin käsittely routeille
#make_response -objektilla voidaan lisätä 'header' -tietojen käsittely pyynnöille
from flask import render_template,request,make_response,flash,redirect,session
#from app.forms import FriendForm,LoginForm,RegisterForm
from app import db
from app.db_models import Users,Friends
from flask.ext.bcrypt import check_password_hash

"""   Tämä korvattu auth -blueprintillä. Huom! import forms.
@app.route('/',methods=['GET','POST'])
def index():
    login = LoginForm()
    if request.method == 'GET':
        return render_template('template_index.html',form=login,isLogged=False)
    else:
        #Check if form data is valid
        if login.validate_on_submit():
            #Check if correct username and password
            #user = Users.query.filter_by(email=login.email.data).filter_by(passw=login.passw.data) #Tämä versio ei sisällä salauksen purkua
            user = Users.query.filter_by(email=login.email.data)
            print(user)
            #if user.count() == 1 #Tämä versio ei sisällä passw salauksen purkua
            if (user.count() == 1 and (check_password_hash(user[0].passw,login.passw.data))):
                print(user[0])
                session['user_id'] = user[0].id
                session['isLogged'] = True
                #tapa 1
                friends = Friends.query.filter_by(user_id=user[0].id)
                print(friends)
                return render_template('template_user.html',isLogged=True,friends=friends)
            else:
                flash('Wrong email or password')
                return render_template('template_index.html',form=login,isLogged=False)
                #return redirect('/') toimisi myös
        #form data was not valid
        else:
            flash('Give proper information to email and password fields')
            return render_template('template_index.html',form=login,isLogged=False)
"""

    #name = 'Jussi'
    #address = 'Jokukatu 1'
    #response = make_response(render_template('template_index.html',name=name,title=address))
    #response.headers.add('Cache-Control','no-cache')
    #return response
    #return render_template('template_index.html',title=address,name=name)
    #return 'Hello World'        

"""   Tämä korvattu auth -blueprintillä      
@app.route('/register',methods=['GET','POST'])
def registerUser():
    form = RegisterForm()
    if request.method == 'GET':
        return render_template('template_register.html',form=form,isLogged=False)
    else:
        if form.validate_on_submit():
            user = Users(form.email.data,form.passw.data)
            try:
                db.session.add(user)
                db.session.commit()
            except:
                db.session.rollback() #rollback ottaa tiedon pois, jos jotain ehti mennä tietokantaan. Kutsutaan myös  automaattisesti, joten ei välttämättä tarvi kirjoittaa
                flash('Username allready in use')
                return render_template('template_register.html',form=form,isLogged=False)
            flash('Name {0} registered'.format(form.email.data))
            return redirect('/')
        else:
            flash('Invalid email address or password missing')
            return render_template('template_register.html',form=form,isLogged=False)
"""

"""   Tämä korvattu blueprintillä
@app.route('/friends',methods=['GET','POST'])
def friends():
    #Check that user is logged in before you let execute this route
    if not('isLogged' in session or session['isLogged'] == False):
        return redirect('/')
    form = FriendForm()
    if request.method == 'GET':
        return render_template('template_friends.html',form=form,isLogged=True)
    else:
        if form.validate_on_submit():
            temp = Friends(form.name.data,form.address.data,form.age.data,session['user_id'])
            db.session.add(temp)
            db.session.commit()
            #tapa 2: 
                #Users -modeliin on määritetty db.relationship -> sisältää friends -tiedot
            user = Users.query.get(session['user_id']) #Luo päivitetyn friends -listan ja alla renderöi sen uudelleen
            print(user.friends)
            return render_template('template_user.html',isLogged=True,friends=user.friends)
        else:
            flash('Give proper values to all fields')
            return render_template('template_friends.html',form=form,isLogged=True)
"""
  
"""
@app.route('/logout')
def logout():
    #Delete user session (clear all values)
    session.clear()
    return redirect('/')
"""
        
@app.route('/user/<username>')
def user(username):
    print(request.headers.get('User-Agent'))
    print(request.headers.get('Accept-Language'))
    print(request.headers.get('Accept-Encoding'))
    return render_template('template_user.html',name=username)

#Example how you can define route methods
#Tälle routelle voidaan lähettää dataa GET ja POST -metodeilla. GET on default, jos ei ole määritetty.
@app.route('/user',methods=['GET','POST'])
def userParams():
    name = request.args.get('name')   #luetaan /user -kontekstiin tulevasta pyynnöstä attribuutti 'name'
    return render_template('template_user.html',name=name)

