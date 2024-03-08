from flask import Flask, render_template, request, redirect, url_for
import sqlite3

'''
Red underlines? Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''

app = Flask(__name__)

# Initiate a connection to the database
db = sqlite3.connect("books-collection.db")
cursor = db.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS books \
    (id INTEGER PRIMARY KEY, \
    title varchar(250) NOT NULL UNIQUE, \
    author varchar(250) NOT NULL, \
    rating FLOAT NOT NULL)")
# cursor.execute("INSERT INTO books VALUES(1, 'Harry Potter', 'J. K. Rowling', '9.3')")
# db.commit()


all_books = []

@app.route('/')
def home():
    return render_template("index.html", books=all_books)


@app.route("/add", methods=["POST", "GET"])
def add():
    if request.method == "POST":
        book_name = request.form["book_name"]
        book_author = request.form["book_author"]
        rating = request.form["rating"]
        new_book = {
            "name": book_name,
            "author": book_author,
            "rating": rating
        }
        all_books.append(new_book)
        print(all_books)
        return redirect(url_for('home'))
    return render_template("add.html")

if __name__ == "__main__":
    app.run()

