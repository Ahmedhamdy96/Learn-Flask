'''
Before Running :
[ 1 ] $ export FLASK_APP=my_app.py    => to tell your terminal the application to work with by exporting the FLASK_APP environment variable .
[ 2 ] $ export FLASK_ENV=development  => To enable all development features including debug mode
[ 3 ] $ flask run                     => To Run The Code

'''

from flask import Flask                  # import Flask Class
app = Flask(__name__)                    # creating a Flask Object , __name__ is the curent file -app- name

@app.route("/")                          # decorator to tell Flask what URL should trigger home() function
def home():
    return " welcome to home page "
