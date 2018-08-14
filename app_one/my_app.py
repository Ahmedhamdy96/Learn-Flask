'''
Before Running :
[ 1 ] $ export FLASK_APP=my_app.py    => to tell your terminal the application to work with by exporting the FLASK_APP environment variable .
[ 2 ] $ export FLASK_ENV=development  => To enable all development features including debug mode
[ 3 ] $ flask run                     => To Run The Code

'''

from flask import Flask                  # import Flask Class
app = Flask(__name__)                    # creating a Flask Object , __name__ is the curent file -app- name

@app.route("/")                          # decorator to tell Flask what URL should trigger home() function
@app.route("/home")                      # another decorator to run the home() function => 127.0.0.1:5000/ = 127.0.0.1:5000/home
def home():
    return " welcome to home page "




#  [ 1 ] If you enable debug support the server will reload itself on code changes,and it will also provide you with a helpful debugger if things go wrong.
#  [ 2 ] This if __name__=='__main__'      => To run the code with  [ $python3 my_app.py ] instead of [ $flask run ]
if __name__=='__main__':
    app.run(debug=True)
