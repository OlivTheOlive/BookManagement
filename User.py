from Book import Book
class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.borrowed_books = []

    def get_name(self):
        return self.name

    def get_email(self):
        return self.email

    def borrow_book(self, book):
        self.borrowed_books.append(book)

    def return_book(self, book):
        if book in self.borrowed_books:
            self.borrowed_books.remove(book)


userTest = User("John","test@email.com")
book1 = Book("Python Programming", "John Smith", 2022, 101)
print(userTest.get_name())
print(userTest.get_email())
print(userTest.borrowed_books)




    