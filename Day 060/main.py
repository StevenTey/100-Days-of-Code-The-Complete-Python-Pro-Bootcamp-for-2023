from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def receive_data():
    error = None
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        # print(f"Name: {username}, Password :{password}")
    else:
        error = 'Invalid username/password'
    return f"<h1>Name: {username}, Password :{password}</h1>"

if __name__ == '__main__':
    app.run(debug=True)