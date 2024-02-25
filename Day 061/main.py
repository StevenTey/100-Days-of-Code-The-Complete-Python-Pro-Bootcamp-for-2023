from flask import Flask, render_template
from flask_wtf import FlaskForm
import email_validator
from flask_bootstrap import Bootstrap5
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length

'''
Red underlines? Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''


class LoginForm(FlaskForm):
    email = StringField(label = 'Email', validators = [DataRequired(), Email(message="Please enter a valid email.")])
    password = PasswordField(label = 'Password', validators = [DataRequired(), Length(min=8, message="Password must be at least 8 characters long.")])
    submit = SubmitField(label = 'Log In')

app = Flask(__name__)
bootstrap = Bootstrap5(app)
app.secret_key = "secret-is-secret"

EMAIL = "admin@email.com"
PASSWORD = "12345678"

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/login", methods=['GET', 'POST'])
def login():
    login_form = LoginForm()
    if login_form.validate_on_submit() :
        if login_form.email.data == EMAIL and login_form.password.data == PASSWORD:
            return render_template('success.html')
        else:
            return render_template('denied.html')
    return render_template('login.html', form = login_form)

if __name__ == '__main__':
    app.run(debug=True)
