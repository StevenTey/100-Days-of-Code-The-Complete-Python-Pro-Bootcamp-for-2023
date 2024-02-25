from flask import Flask, render_template, request
import random
import datetime
import requests

app = Flask(__name__)

@app.route('/')
def home():
    random_number = random.randint(1, 10)
    year = datetime.datetime.now().year
    return render_template('index.html', rnum=random_number, current_year=year, name = "Steven")

@app.route('/guess/<name>')
def guess(name):
    # Calling agify API to get age prediction
    age_url = f"https://api.agify.io"
    age_param = {
        "name": name
    }
    age_response = requests.get(age_url, params=age_param)
    age = age_response.json().get('age')
    
    # Call genderize api to get gender prediction
    gender_url = f"https://api.genderize.io"
    gender_param = {
        "name": name
    }
    gender_response = requests.get(gender_url, params = gender_param)
    gender = gender_response.json().get('gender')
    
    return render_template('index_g.html', name=name.title(), age = age, gender = gender)

@app.route('/blog/<num>')
def get_blog(num):
    blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
    try:
        response = requests.get(blog_url)
        response.raise_for_status()  # This will raise an HTTPError if the HTTP request returned an unsuccessful status code
        all_posts = response.json()
    except requests.exceptions.RequestException as e:
        print(e)
        all_posts = []  # Set to an empty list or handle the error as appropriate
    return render_template('blog.html', posts = all_posts)



if __name__ == '__main__':
    app.run(debug=True)