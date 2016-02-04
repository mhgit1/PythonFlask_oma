from flask import Blueprint,render_template,request,flash,redirect,session,make_response
from blueprint.ud.ud_forms import FriendForm
from app import db
from app.db_models import Users,Friends
from werkzeug import secure_filename

#Create blueprint
#First argumetn is the name of the blueprint folder
#Secon is always __name__ attribute
#Third parameter tells what folder contains your templates
#url_prefix('/app/') määrittää yleisen prefixin kaikille routeille, niin ei tarvitse kirjoittaa kokonaan jokaiseen. Ei välttämätön
ud = Blueprint('ud',__name__,template_folder='templates',url_prefix=('/app/'))

#/app/delete
@ud.route('delete/<int:id>')
def delete(id):
    return "Delete"

@ud.route('update')
def update():
    return "Update"

@ud.route('friends',methods=['GET','POST'])
def friends():
    form = FriendForm()
    if request.method == 'GET':
        return render_template('template_friends.html',form=form,isLogged=True)
    else:
        if form.validate_on_submit():
            temp = Friends(form.name.data,form.address.data,form.age.data,session['user_id'])
            #Save the image if present
            if form.upload_file.data:
                filename = secure_filename(form.upload_file.data.filename)
                form.upload_file.data.save('app/static/images/' + filename)
                temp.filename = '/static/images/' + filename
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


def before_request():
    if not 'isLogged' in session:
        return redirect('/')

#Määrittää, että def before_request(): -funktiota kutsutaan aina ensimmäisen ennen minkään routen suorittamista. 
#(session -objektissa on olemassa before_request -moduuli)
ud.before_request(before_request) 