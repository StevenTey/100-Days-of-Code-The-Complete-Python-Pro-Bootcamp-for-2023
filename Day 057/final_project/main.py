from flask import Flask, render_template
import requests
from post import Post

app = Flask(__name__)

# Fake blog
blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
blog_response = requests.get(blog_url)
blog_posts = blog_response.json()
post_objects = []
for blog in blog_posts:
    post_obj = Post(blog["id"], blog["title"], blog["subtitle"], blog["body"])
    post_objects.append(post_obj)

@app.route('/')
def home():
    return render_template("index.html", posts=post_objects)

@app.route('/blog/<int:num>')
def get_blog(num):
    blog_post = post_objects[num-1]
    return render_template("post.html", post_id=num, post = blog_post)

if __name__ == "__main__":
    app.run(debug=True)

