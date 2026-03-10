import json
from models import Library, Book, Member, BookStatus, Loan
from datetime import date

def save_data(lib):
    data = {
        "books": {
            isbn: {
                "isbn": b.isbn,
                "title": b.title,
                "author": b.author,
                "status": b.status.value
            }
            for isbn, b in lib.books.items()
        },
        "members": {
            mid: {
                "member_id": m.member_id,
                "name": m.name,
                "email": m.email,
                "borrowed_isbns": m.borrowed_isbns
            }
            for mid, m in lib.members.items()
        },
        "loans": [
            {
                "isbn": l.isbn,
                "member_id": l.member_id,
                "borrowed_on": l.borrowed_on.isoformat(),
                "due_date": l.due_date.isoformat(),
                "returned_on": l.returned_on.isoformat() if l.returned_on else None
            }
            for l in lib.loans
        ]
    }
    with open("data.json", "w") as f:
        json.dump(data, f, indent=4)

def load_data(lib):
    try:
        with open("data.json", "r") as f:
            data = json.load(f)
            for b in data["books"].values():
                lib.add_book(Book(
                    isbn=b["isbn"],
                    title=b["title"],
                    author=b["author"],
                    status=BookStatus(b["status"])
                ))
            for m in data["members"].values():
                lib.add_member(Member(
                    member_id=m["member_id"],
                    name=m["name"],
                    email=m["email"],
                    borrowed_isbns=m["borrowed_isbns"]
                ))
            for l in data["loans"]:
                lib.loans.append(Loan(
                    isbn=l["isbn"],
                    member_id=l["member_id"],
                    borrowed_on=date.fromisoformat(l["borrowed_on"]),
                    due_date=date.fromisoformat(l["due_date"]),
                    returned_on=date.fromisoformat(l["returned_on"]) if l["returned_on"] else None
                ))
    except FileNotFoundError:
        pass
