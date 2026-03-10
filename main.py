from models import Library, Book, Member

def main():
    lib = Library()

    while True:
        print("\n--- Library Menu ---")
        print("1. Add book")
        print("2. Add member")
        print("3. Borrow book")
        print("4. Quit")

        choice = input("Choose an option: ")

        if choice == "1":
            isbn = input("ISBN: ")
            title = input("Title: ")
            author = input("Author: ")
            lib.add_book(Book(isbn=isbn, title=title, author=author))
            print("Book added!")

        elif choice == "2":
            member_id = input("Member ID: ")
            name = input("Name: ")
            email = input("Email: ")
            lib.add_member(Member(member_id=member_id, name=name, email=email))
            print("Member added!")

        elif choice == "3":
            isbn = input("ISBN: ")
            member_id = input("Member ID: ")
            lib.borrow_book(isbn, member_id)

        elif choice == "4":
            print("Goodbye!")
            break

if __name__ == "__main__":
    main()
