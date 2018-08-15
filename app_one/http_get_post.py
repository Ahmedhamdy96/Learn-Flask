from flask import Flask
from flask import request # includes GET and POST HTTP Methods

app = Flask(__name__)

@app.route('/')
def home():
    if request.method == 'POST' :
        return "You POST (send) data to Server "
    else :
        return "You GET data from the server "

if __name__ == '__main__':
    app.run(debug=True)
