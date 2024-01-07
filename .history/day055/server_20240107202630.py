from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return '<h1">Guess a number between 0 and 9</h1>\
        <p> </p>\
        <img src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif" width=300>'
        
if __name__ == '__main__':
    # Run the app in debug mode to auto-reload
    app.run(debug=True)