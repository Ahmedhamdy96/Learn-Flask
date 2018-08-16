from flask import Flask
from flask import render_template   # to render html , css , js files

from os import urandom #  urandom(16) => to generate a secret key os 16 chars for example same as token_bytes(16) =>> urandom(16).hex()
from forms import RegistrationForm , LoginForm

app = Flask(__name__)
# app.config['SECRET_KEY'] = '' # urandom(16).hex() => at Desktop / key 
#====================================================================================
posts = [
        {'title':'Python vs C ',
         'name':'ahmed' ,
         'date':'August 2018' ,
         'post':'I Love both Python and C  '
         } ,
         {
         'title' : 'Coffe vs Tea ' ,
         'name':'Mohamed' ,
         'date':'August 2018' ,
         'post':'My name is mohamed and i love coffe more than tea'
         }
        ]
@app.route('/')
def home():
    return render_template('home.html' , posts=posts) # we have access to that variable (posts) in the home.html template

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/regestration')
def regestration():
    form = RegistrationForm() # creating an instance of the RegistrationForm Class
    return render_template('registration.html'  , title = 'Registration' , form = form )
    # form = form make us able to accecc the RegistrationForm object in the html template

@app.route('/login')
def login():
    form = LoginForm()  # creating an object of the login form and name it form
    return render_template('login.html' , title = 'Login' , form = form) # we can access this object at the html by the name form
#=====================================================================================
if __name__=='__main__':
    app.run(debug=True)
