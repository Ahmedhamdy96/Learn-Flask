from flask import Flask
from flask import render_template   # to render html , css , js files
app = Flask(__name__)
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
#=====================================================================================
if __name__=='__main__':
    app.run(debug=True)
