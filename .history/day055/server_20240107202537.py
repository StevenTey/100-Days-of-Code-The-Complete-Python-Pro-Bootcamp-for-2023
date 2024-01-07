from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return '<h1">Guess a number between 0 and 9</h1>\
        <p>This is a paragraph</p>\
        <img src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif" width=200>'