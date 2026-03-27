class Book:
    def __init__(self, book_id, title):
        self.book_id = book_id
        self.title = title
        self.is_issued = False


class Member:
    def __init__(self, member_id, name):
        self.member_id = member_id
        self.name = name


class Library:
    def __init__(self):
        self.books = []
        self.members = []

    def add_book(self):
        book_id = int(input("Enter Book ID: "))
        title = input("Enter Book Title: ")
        self.books.append(Book(book_id, title))
        print("Book added successfully!")

    def add_member(self):
        member_id = int(input("Enter Member ID: "))
        name = input("Enter Member Name: ")
        self.members.append(Member(member_id, name))
        print("Member added successfully!")

    def issue_book(self):
        book_id = int(input("Enter Book ID to issue: "))
        for book in self.books:
            if book.book_id == book_id:
                if not book.is_issued:
                    book.is_issued = True
                    print("Book issued successfully!")
                else:
                    print("Book already issued!")
                return
        print("Book not found!")

    def return_book(self):
        book_id = int(input("Enter Book ID to return: "))
        for book in self.books:
            if book.book_id == book_id:
                if book.is_issued:
                    book.is_issued = False
                    print("Book returned successfully!")
                else:
                    print("Book was not issued!")
                return
        print("Book not found!")

    def display_books(self):
        print("\n--- Book List ---")
        for book in self.books:
            status = "Issued" if book.is_issued else "Available"
            print(book.book_id, "-", book.title, "-", status)



lib = Library()

while True:
    print("\n--- Library Menu ---")
    print("1. Add Book")
    print("2. Add Member")
    print("3. Issue Book")
    print("4. Return Book")
    print("5. Display Books")
    print("6. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        lib.add_book()
    elif choice == 2:
        lib.add_member()
    elif choice == 3:
        lib.issue_book()
    elif choice == 4:
        lib.return_book()
    elif choice == 5:
        lib.display_books()
    elif choice == 6:
        print("Exiting...")
        break
    else:
        print("Invalid choice!")