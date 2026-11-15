class Book:
    def __init__(self, book_id, title, author, quantity):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.quantity = quantity


class Library:
    def __init__(self):
        self.books = []
        self.issued_books = []

    # Add a new book
    def add_book(self):
        book_id = input("Enter Book ID: ")

        for book in self.books:
            if book.book_id == book_id:
                print("Book ID already exists!")
                return

        title = input("Enter Book Title: ")
        author = input("Enter Author Name: ")

        try:
            quantity = int(input("Enter Quantity: "))

            if quantity <= 0:
                print("Quantity must be a positive number!")
                return

        except ValueError:
            print("Please enter a valid whole number!")
            return

        new_book = Book(book_id, title, author, quantity)
        self.books.append(new_book)

        print("Book added successfully!")

    # Display all books
    def view_books(self):
        if not self.books:
            print("No books available in the library.")
            return

        print("\n===== ALL BOOKS =====")

        for book in self.books:
            print("Book ID:", book.book_id)
            print("Title:", book.title)
            print("Author:", book.author)
            print("Available Quantity:", book.quantity)
            print("----------------------")

    # Search book by ID or title
    def search_book(self):
        search = input("Enter Book ID or Title: ").lower()
        found = False

        for book in self.books:
            if book.book_id.lower() == search or book.title.lower() == search:
                print("\nBook Found!")
                print("Book ID:", book.book_id)
                print("Title:", book.title)
                print("Author:", book.author)
                print("Available Quantity:", book.quantity)
                found = True

        if not found:
            print("Book not found!")

    # Issue a book
    def issue_book(self):
        book_id = input("Enter Book ID: ")

        for book in self.books:
            if book.book_id == book_id:

                if book.quantity > 0:
                    student = input("Enter Student Name: ")

                    book.quantity -= 1

                    record = {
                        "book_id": book_id,
                        "title": book.title,
                        "student": student
                    }

                    self.issued_books.append(record)

                    print("Book issued successfully!")
                    print("Available Quantity:", book.quantity)
                    return

                else:
                    print("Sorry! Book is not available.")
                    return

        print("Book ID not found!")

    # Return a book
    def return_book(self):
        book_id = input("Enter Book ID: ")
        student = input("Enter Student Name: ")

        for record in self.issued_books:
            if (record["book_id"] == book_id and
                    record["student"].lower() == student.lower()):

                for book in self.books:
                    if book.book_id == book_id:
                        book.quantity += 1
                        break

                self.issued_books.remove(record)

                print("Book returned successfully!")
                return

        print("No matching issued book record found!")

    # Delete a book
    def delete_book(self):
        book_id = input("Enter Book ID to delete: ")

        for record in self.issued_books:
            if record["book_id"] == book_id:
                print("Cannot delete! Book is currently issued.")
                return

        for book in self.books:
            if book.book_id == book_id:
                self.books.remove(book)
                print("Book deleted successfully!")
                return

        print("Book not found!")

    # Display issued books
    def view_issued_books(self):
        if not self.issued_books:
            print("No books are currently issued.")
            return

        print("\n===== ISSUED BOOKS =====")

        for record in self.issued_books:
            print("Book ID:", record["book_id"])
            print("Book Title:", record["title"])
            print("Student Name:", record["student"])
            print("----------------------")


# Main program
library = Library()

while True:

    print("\n===== LIBRARY MANAGEMENT SYSTEM =====")
    print("1. Add Book")
    print("2. View All Books")
    print("3. Search Book")
    print("4. Issue Book")
    print("5. Return Book")
    print("6. Delete Book")
    print("7. View Issued Books")
    print("8. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        library.add_book()

    elif choice == "2":
        library.view_books()

    elif choice == "3":
        library.search_book()

    elif choice == "4":
        library.issue_book()

    elif choice == "5":
        library.return_book()

    elif choice == "6":
        library.delete_book()

    elif choice == "7":
        library.view_issued_books()

    elif choice == "8":
        print("Thank you for using Library Management System!")
        break

    else:
        print("Invalid choice! Please select between 1 and 8.")