from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return '<h1 style="text-align: center">Hello, World!</h1>\
        <p>This is a paragraph</p>\
        <img src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif" width=200>'

@app.route('/bye')
def hello():
    return 'Bye, World!'

@app.route('/<name>')
def greet(name):
    return f"Hello, there {name}!"

if __name__ == '__main__':
    # Run the app in debug mode to auto-reload
    app.run(debug=True)