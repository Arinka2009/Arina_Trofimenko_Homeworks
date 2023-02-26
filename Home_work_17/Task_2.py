# 2nd Task

class Library:
    def __init__(self, name: str):
        self.name = name
        self.books = []
        self.authors = []

    def new_book(self, name: str, year: int, author: 'Author') -> 'Book':
        book = Book(name, year, author)  # create exemplar of Book class

        self.books.append(book)  # add book to the library books list

        if author not in self.authors:  # add author to the library authors list
            self.authors.append(author)

        author.books.append(book)  # add the book to the author's books list
        return book

    def group_by_author(self, author: 'Author') -> list:
        return [book for book in self.books if book.author == author]

    def group_by_year(self, year: int) -> list:
        return [book for book in self.books if book.year == year]

    def __str__(self):
        return f'Library: {self.name} includes: {len(self.books)} Books and {len(self.authors)} Authors.'

    def __repr__(self):
        return f'{self.__class__}: {self.name}'


class Book:
    count = 0

    def __init__(self, name, year, author: 'Author'):
        self.name = name
        self.year = year
        self.author = author
        Book.count += 1

    def __repr__(self):
        return f'{self.name}, {self.year}, {self.author}'

    def __str__(self):
        return f'Book: {self.name}, Year: {self.year}, Author: {self.author.name}'


class Author:
    def __init__(self, name: str, country: str, birthday: str):
        self.name = name
        self.country = country
        self.birthday = birthday
        self.books = []

    def __repr__(self):
        return f'{self.name}, {self.country}, {self.birthday}'

    def __str__(self):
        return f'Author: {self.name}, Country: {self.country}, Birthday: {self.birthday}'


# Create exemplars for code checking
library = Library('Central Library')

author1 = Author('Joanne Rowling', 'UK', 'July 31, 1965')
author2 = Author('George Martin', 'USA', 'September 20, 1948')

book1 = library.new_book("Harry Potter and the Philosopher's Stone", 1997, author1)
book2 = library.new_book("Harry Potter and the Chamber of Secrets", 1998, author1)
book3 = library.new_book("A Song of Ice and Fire", 1996, author2)
book4 = library.new_book("A Clash of Kings", 1998, author2)
