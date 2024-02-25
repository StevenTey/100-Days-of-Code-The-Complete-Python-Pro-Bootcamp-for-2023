from flask import Flask, render_template, url_for
import requests


app = Flask(__name__)
# url = url_for('static', filename='./static/style.css')

@app.route('/')
def index():
    URL = "https://api.npoint.io/204ecabb335161163aed"
    try:
        response = requests.get(URL)
        response.raise_for_status()
        blogs = response.json()
    except requests.exceptions.RequestException as e:
        print(e)
        blogs = []
    return render_template('index.html', all_posts = blogs)

@app.route('/about')
def about():
    return render_template('about.html', title='About')

@app.route('/contact')
def contact():
    return render_template('contact.html', title='Contact')

@app.route('/post/<int:post_id>')
def get_post(post_id):
    URL = "https://api.npoint.io/204ecabb335161163aed"
    try:
        response = requests.get(URL)
        response.raise_for_status()
        blogs = response.json()
    except requests.exceptions.RequestException as e:
        print(e)
        blogs = []
    return render_template('post.html', title='Post', num=post_id, post=blogs[post_id-1])

if __name__ == "__main__":
    app.run(debug=True)
    