import random
from flask import Flask
app = Flask(__name__)

# wrapper functions - making bold, emphasis, and underlined
def make_bold(function):
    def wrapper_function():
        return "<b>" + function() + "</b>"
    return wrapper_function

def make_emphasis(function):
    def wrapper_function():
        return "<em>" + function() + "</em>"
    return wrapper_function

def make_underlined(function):
    def wrapper_function():
        return "<u>" + function() + "</u>"
    return wrapper_function

@app.route('/')
@make_bold
@make_emphasis
def hello_world():
    random_number = random.randint(0, 9)
    return '<h1 style="font-size: 24px;">Guess a number between 0 and 9</h1>\
        <p> </p>\
        <img src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif" width=300>'



if __name__ == '__main__':
    # Run the app in debug mode to auto-reload
    app.run(debug=True)