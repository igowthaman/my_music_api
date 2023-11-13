from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello, Music'

@app.route('/about')
def about():
    return 'About'