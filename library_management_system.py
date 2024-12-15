import json

class Library():
    def __init__(self, filename="library.json"):
        self.books = []
        self.filename = filename
        self.load_books()
    
    def save_book(self):
        data = [{
            "title": book.title,
            "author": book.author,
            "isbn": book.isbn,
            "is_borrowed": book.is_borrowed
        } for book in self.books]

        with open(self.filename, "w") as f:
            json.dump(data, f, indent = 4)

    def add_book(self,book):
        for existing_book in self.books:
            if existing_book.isbn == book.isbn:
                print(f"The book with ISBN: {book.isbn} is already in the Library")
                return
        self.books.append(book)
        self.save_book()
        print("Book added Successfully")

    def remove_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                self.books.remove(book)
                self.save_book()
                print(f"Removed: {book.title}")
                return True
        return False
    
    def load_books(self):
        try:
            with open(self.filename, "r") as file:
                data = json.load(file)
                for book_data in data:
                    book = Book(book_data["title"], book_data["author"], book_data["isbn"])
                    book.is_borrowed = book_data["is_borrowed"]
                    self.books.append(book)
        except FileNotFoundError:
            print("No previous library data found")
        except json.JSONDecodeError:
            print("Error reading the library data from file. Please try again")

    def show_books(self):
        if not self.books:
            print("No books available.")
        else:
            for book in self.books:
                status = "Available" if not book.is_borrowed else "Borrowed"
                print(f"{book.title} by {book.author} (ISBN: {book.isbn}) - {status}")

class Book():
    def __init__(self,title,author,isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_borrowed = False
    
    def borrow(self):
        if not self.is_borrowed:
            self.is_borrowed = True
            print(f"You borrowed : {self.title}")
            return True
        else:
            print(f"{self.title} is already borrowed")
            return False
    
    def return_book(self):
        if self.is_borrowed:
            self.is_borrowed = False
            print(f"You returned: {self.title}")
            return True
        else:
            print(f"{self.title} was not borrowed")
            return False

def library_system():
    library = Library()

    while True:
        print("\n1. Add Book")
        print("2. Remove Book")
        print("3. Show All Books")
        print("4. Borrow Books")
        print("5. Return Book")
        print("6. Exit")

        choice = input("\nChoose an option: ")
        if choice == '1':
            title = input("Enter book title: ")
            author = input("Enter author: ")
            isbn = input("Enter ISBN: ")
            book = Book(title, author, isbn)
            library.add_book(book)
        elif choice == '2':
            isbn = input("Enter ISBN to remove: ")
            library.remove_book(isbn)
        elif choice == '3':
            library.show_books()
        elif choice == '4':
            isbn = input("Enter ISBN to borrow: ")
            for book in library.books:
                if book.isbn == isbn:
                    if book.borrow():
                        library.save_book()
                    break
            else:
                print("Book not found.")
        elif choice == '5':
            isbn = input("Enter the ISBN to return")
            for book in library.books:
                if book.isbn == isbn:
                    if book.return_book():
                        library.save_book()
                    break
            else:
                print("Book not found")
        elif choice == '6':
            break
        else:
            print("Invalid Input pleae choose right one")

library_system()