class Book:
    def __init__(self, title, author, year, bookId):
        self.title = title
        self.author = author
        self.year = year
        self.bookId = bookId

    def get_title(self):
        return self.title
    def get_author(self):
        return self.author
    def get_year(self):
        return self.year
    def get_bookId(self):
        return self.bookId
    

#book1=Book("Love is Blind","John Doe", 1999)

#print(book1.get_author())
#print(book1.get_title())
#print(book1.get_year())