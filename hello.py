from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return '<h1>Hello, World!</h1>'

@app.route('/user/<name>')
def user(name):
    return '<h1>Привет , %s !</h1>'
