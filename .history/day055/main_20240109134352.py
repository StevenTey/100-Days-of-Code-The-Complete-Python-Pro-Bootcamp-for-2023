from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return '<h1 style="text-align: center">Hello, World!</h1>\
        <p>This is a paragraph</p>\
        <img src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif" width=200>'

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

@app.route('/bye')
@make_bold
@make_emphasis
@make_underlined
def hello():
    return '<b>Bye!!</b>'

@app.route('/<name>')
def greet(name):
    return f"Hello, there {name}!"

class User:
    def __init__(self, name):
        self.name = name
        self.is_logged_in = False

def is_authenticated_decorator(function):
    def wrapper(*args, **kwargs):
        if args[0].is_logged_in == True:
            function(args[0])
    return wrapper

@is_authenticated_decorator
def create_blog_post(user):
    print(f"This is {user.name}'s new blog post.")

new_user = User("angela")
new_user.is_logged_in = True
create_blog_post(new_user)

if __name__ == '__main__':
    # Run the app in debug mode to auto-reload
    app.run(debug=True)

# TODO: Create the logging_decorator() function 👇
def logging_decorator(function):
  def wrapper(*args):
    print(f"You called {function.__name__}{args}")
    result = function(args[0], args[1], args[2])
    print(f"It returned: {result}")
  return wrapper

# TODO: Use the decorator 👇
@logging_decorator
def a_function(a, b, c):
  return a * b * c

# testing
a_function(inputs[0], inputs[1], inputs[2])

