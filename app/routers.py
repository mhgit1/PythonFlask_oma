from app import app 
"""Monirivinen kommentti: Ensimmäinen app viittaa app -kansioon 
    ja toinen __init__.py -tiedostossa määritettyyn app -nimeen"""
#Yksirivinen kommentti: importilla voi tuoda toisessa tiedostossa määritettyjä moduuleja

#render_template gives you access to Jinja2 template engine
#request -objektilla saadaan requestin käsittely routeille
#make_response -objektilla voidaan lisätä 'header' -tietojen käsittely pyynnöille
from flask import render_template,request,make_response,flash,redirect
from app.forms import LoginForm,RegisterForm,AddfriendForm
from app import db
from app.db_models import Users,Friends

@app.route('/',methods=['GET','POST'])
def index():
    login = LoginForm()
    if request.method == 'GET':
        return render_template('template_index.html',form=login)
    else:
        #Check if form data is valid
        if login.validate_on_submit():
            print(login.email.data)
            print(login.passw.data)
            return render_template('template_user.html')
        #form data was not valid
        else:
            flash('Give proper information to email and password fields')
            return render_template('template_index.html',form=login)

    #name = 'Jussi'
    #address = 'Jokukatu 1'
    #response = make_response(render_template('template_index.html',name=name,title=address))
    #response.headers.add('Cache-Control','no-cache')
    #return response
    #return render_template('template_index.html',title=address,name=name)
    #return 'Hello World'        

        
@app.route('/register',methods=['GET','POST'])
def registerUser():
    form = RegisterForm()
    if request.method == 'GET':
        return render_template('template_register.html',form=form)
    else:
        if form.validate_on_submit():
            user = Users(form.email.data,form.passw.data)
            db.session.add(user)
            db.session.commit()
            flash('Name {0} registered'.format(form.email.data))
            return redirect('/')
        else:
            flash('Invalid email address or password missing')
            return render_template('template_register.html',form=form)

    
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


@app.route('/addfriend',methods=['GET','POST'])
def addFriend():
    form = AddfriendForm()
    if request.method == 'GET':
        return render_template('template_addfriend.html',form=form)
    else:
        if form.validate_on_submit():
            friend = Friends(form.name.data,form.address.data,form.age.data)
            db.session.add(friend)
            db.session.commit()
            flash('Friend registered')
            return redirect('/user')
        else:
            flash('Invalid data')
            return render_template('template_addfriend.html',form=form)