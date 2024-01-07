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
    user_input = input("Guess a number between 0 and 9: ")
    if user_input.isdigit() and 0 <= int(user_input) <= 9:
        user_number = int(user_input)
        if user_number == number:
            return "<h1 style='font-size: 24px;'>Congratulations! You guessed the correct number.</h1>"
        else:
            return "<h1 style='font-size: 24px;'>Wrong guess. Try again!</h1>"
    else:
        return "<h1 style='font-size: 24px;'>Invalid input. Please enter a number between 0 and 9.</h1>"

if __name__ == '__main__':
    # Run the app in debug mode to auto-reload
    app.run(debug=True)

 
if __name__ == '__main__':
    # Run the app in debug mode to auto-reload
    app.run(debug=True)