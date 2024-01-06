from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/bye')
def hello():
    return 'Bye, World!'

if app == '__main__':
    app.run()