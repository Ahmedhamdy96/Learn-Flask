from flask import Flask
from flask import url_for    # url_for('Function Name')

app = Flask(__name__)

@app.route('/')
def home():
    return " > > > HOME PAGE < < < "

@app.route('/about/users/ahmed')
def show_info():
    return "Ahmed hamdy "

with app.test_request_context():
    print(url_for('home'))
    print(url_for('show_info'))

if __name__=='__main__':
    app.run()
