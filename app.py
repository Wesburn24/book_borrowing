from flask import Flask, render_template, request, redirect
from models import Library, Book, Member
from storage import save_data, load_data

app = Flask(__name__)
lib = Library()
load_data(lib)

@app.route("/")
def index():
    return render_template("index.html", books=lib.books, members=lib.members)

@app.route("/add_book", methods=["POST"])
def add_book():
    isbn = request.form["isbn"]
    title = request.form["title"]
    author = request.form["author"]
    lib.add_book(Book(isbn=isbn, title=title, author=author))
    save_data(lib)
    return redirect("/")

@app.route("/add_member", methods=["POST"])
def add_member():
    member_id = request.form["member_id"]
    name = request.form["name"]
    email = request.form["email"]
    lib.add_member(Member(member_id=member_id, name=name, email=email))
    save_data(lib)
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)
