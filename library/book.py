"""module handles the book objects and their sorting when needed."""
from dataclasses import dataclass


@dataclass
class Book:
    """Contains data on books"""
    book_name: str
    author_name: str
    isbn: int
    pub_year: int

    def __lt__(self, other):
        return self.pub_year < other.pub_year

    def __gt__(self, other):
        return self.pub_year > other.pub_year


def sort_books(books: list[Book]) -> list:
    """Sorts a list of book objects by publication year"""
    books_sorted = [book for book in sorted(books, key=lambda book: book.pub_year)]
    return books_sorted

