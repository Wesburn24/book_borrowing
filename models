from dataclasses import dataclass, field
from datetime import date
from enum import Enum

class BookStatus(Enum):
    AVAILABLE = "available"
    BORROWED = "borrowed"
    Reserved = "reserved"

@dataclass
class Book:
    isbn: str
    title: str
    author: str
    status: BookStatus = BookStatus.AVAILABLE

@dataclass
class Member:
    member_id: str
    name: str
    email: str
    borrowed_isbns: list[str] = field(default_factory=list)

@dataclass
class Loan:
    isbn: str
    member_id: str
    borrowed_on: date
    due_date: date
    returned_on: date | None = None

@dataclass
class Library:
    books: dict[str, Book] = field(default_factory=dict)
    members: dict[str, Member] = field(default_factory=dict)
    loans: list[Loan] = field(default_factory=list)

    def add_book(self, book: Book):
        self.books[book.isbn] = book

    def add_member(self, member: Member):
        self.members[member.member_id] = member

    def borrow_book(self, isbn: str, member_id: str):
        book = self.books.get(isbn)
        member = self.members.get(member_id)

        if not book:
            print("Book not found")
            return

        book.status = BookStatus.BORROWED
        loan = Loan(isbn=isbn, member_id=member_id,
                    borrowed_on=date.today(),
                    due_date=date.today().replace(day=date.today().day + 14))
        self.loans,append(loan)
        print(f"{member.name} borrowed {book.title}")


