import requests
from flask import Flask, url_for, request
app = Flask(__name__)

@app.route('/')
def hello_world():
    # Minumun webpage.
    return 'Index Page'

@app.route('/hello')
def hello():
    # Basic usage of route.
    return 'Hello World'

@app.route('/user/<username>')
def show_user_profile(username):
    # Variable.
    return 'User %s' % username

@app.route('/user/<int:userid>')
def show_user_id(userid):
    # Converter.
    return 'User %d' % userid

@app.route('/url_for')
def example_of_url_for():
    # Example of url_for.
    return '<tr>url for hello_world: %s</tr><br> <tr>url for show_user_id: %s</tr>'\
            % (url_for('hello_world'), url_for('show_user_id', userid='1123'))

# HTTP Method
@app.route('/login', methods=['GET', 'POST', 'PUT'])
def login():
    if request.method == 'POST': # from flask import request
        return 'OK' if request.form['user']==request.form['pass'] else 'NOT OK'
    elif request.method == 'PUT':
        f = request.files['the_file']
        f.save('tmp.txt')
        return 'GOT IT'
    else:
        return 'GET'

def test_login():
    r = requests.post('127.0.0.1:5000/login', data={'user':123, 'pass':123})
    print r.text


if __name__ == '__main__':
    app.run('0.0.0.0', debug=True)
