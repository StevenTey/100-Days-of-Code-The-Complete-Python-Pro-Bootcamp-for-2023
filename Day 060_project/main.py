from flask import Flask, render_template, request
import smtplib
import requests

# USE YOUR OWN npoint LINK! ADD AN IMAGE URL FOR YOUR POST. 👇
posts = requests.get("https://api.npoint.io/c790b4d5cab58020d391").json()

file_path = '/Users/weijunsteventey/Documents/password_info.txt'

# Initialize a dictionary to hold your data
data = {}

# Open the file and process each line
with open(file_path, 'r') as file:
    for line in file:
        # Split the line into key and value
        key, value = line.strip().split(' = ')
        
        # Remove the quotes from the value if present
        value = value.strip('"')
        
        # Store in the dictionary
        data[key] = value
        
OWN_EMAIL = data["gmail"]
OWN_PASSWORD = data['password']

app = Flask(__name__)

def send_email(name, email, phone, message):
    email_message = f"Subject:New Message\n\nName: {name}\nEmail: {email}\nPhone: {phone}\nMessage:{message}"
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(OWN_EMAIL, OWN_PASSWORD)
        connection.sendmail(OWN_EMAIL, OWN_EMAIL, email_message)

@app.route('/')
def get_all_posts():
    return render_template("index.html", all_posts=posts)

@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        data = request.form
        data = request.form
        send_email(data["name"], data["email"], data["phone"], data["message"])
        return render_template("contact.html", msg_sent=True)
    return render_template("contact.html", msg_sent=False)

@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    for blog_post in posts:
        if blog_post["id"] == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)

# @app.route("/form-entry")
# def receive_data():
#     return "<h1>Successfully sent your message</h1>"

if __name__ == "__main__":
    app.run(debug=True, port=5001)