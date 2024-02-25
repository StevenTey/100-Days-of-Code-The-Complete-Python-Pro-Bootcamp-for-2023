import random
from flask import Flask
app = Flask(__name__)

# wrapper functions - making bold, emphasis, and underlined
def make_bold(function):
    def wrapper_function():
        return "<b>" + function() + "</b>"
    return wrapper_function

class RandomNumber:
    def __init__(self):
        self.number = random.randint(0, 9)

correct_number = RandomNumber()

@app.route('/')
@make_bold
def hello_world():
    number = correct_number.number
    return '<h1 style="font-size: 24px;">Guess a number between 0 and 9</h1>\
        <p> </p>\
        <img src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif" width=300>'
 
@app.route('/<int:number>')
def guess(number):
    if number == correct_number.number:
        return '<h1 style="color: green;">You found me!</h1>\
            <p> </p>\
            <img src="https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif" width=300>'
    elif number < correct_number.number:
        return '<h1 style="color: red;">Too low, try again!</h1>\
            <p> </p>\
            <img src="https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif" width=300>'
    elif number > correct_number.number:
        return '<h1 style="color: purple;">Too high, try again!</h1>\
            <p> </p>\
            <img src="https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif" width=300>'
 
if __name__ == '__main__':
    # Run the app in debug mode to auto-reload
    app.run(debug=True)