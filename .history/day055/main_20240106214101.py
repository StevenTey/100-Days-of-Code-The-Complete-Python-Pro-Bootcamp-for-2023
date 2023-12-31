from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/bye')
def hello():
    return 'Bye, World!'

@app.route('/<username>')
def greet(name):
    return f"Hello, there {name}!"

if __name__ == '__main__':
    app.run(debug=True)