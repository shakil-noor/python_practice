class Library():
    def __init__(self):
        self.books = []
    
    def add_book(self,book):
        self.books.append(book)
        print("Book added Successfully")

    def remove_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                self.books.remove(book)
                print(f"Removed: {book.title}")
                return True
        return False

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
        else:
            print(f"{self.title} is already borrowed")
    
    def return_book(self):
        if self.is_borrowed:
            self.is_borrowed = False
            print(f"You returned: {self.title}")
        else:
            print(f"{self.title} was not borrowed")

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
                    book.borrow()
                    break
            else:
                print("Book not found.")
        elif choice == '5':
            isbn = input("Enter the ISBN to return")
            for book in library.books:
                if book.isbn == isbn:
                    book.return_book()
                    break
            else:
                print("Book not found")
        elif choice == '6':
            break
        else:
            print("Invalid Input pleae choose right one")

library_system()