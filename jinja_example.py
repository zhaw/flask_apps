import flask

app = flask.Flask(__name__)

@app.route('/')
def index():
    return flask.render_template('index.html',
            my_list=[1,2,3,4], my_string='my string')

app.run('0.0.0.0')
