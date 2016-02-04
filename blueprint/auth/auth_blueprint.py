from flask import Blueprint,render_template,request,flash,redirect,session,make_response
#from app.forms import LoginForm,RegisterForm
from blueprint.auth.auth_forms import LoginForm,RegisterForm
from app import db
from app.db_models import Users,Friends
from flask.ext.bcrypt import check_password_hash

auth = Blueprint('auth',__name__,template_folder='templates')

@auth.route('/',methods=['GET','POST'])
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

        
@auth.route('/register',methods=['GET','POST'])
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

@auth.route('/logout')
def logout():
    #Delete user session (clear all values)
    session.clear()
    flash('Logged out')
    return redirect('/')