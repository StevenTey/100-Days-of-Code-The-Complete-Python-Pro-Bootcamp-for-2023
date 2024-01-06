from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return '<h1> Hello, World!</h1>'

@app.route('/bye')
def hello():
    return 'Bye, World!'

@app.route('/<name>')
def greet(name):
    return f"Hello, there {name}!"

if __name__ == '__main__':
    app.run(debug=True)