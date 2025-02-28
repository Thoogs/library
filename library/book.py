"""module handles the book objects and their sorting when needed."""

from dataclasses import dataclass
from enum import Enum


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


class BookFields(Enum):
    """Enums for book fields in a split csv str"""

    BOOK_NAME = 0
    BOOK_AUTHOR = 1
    BOOK_ISBN = 2
    BOOK_PUB_YEAR = 3


def sort_books(books: list[Book]) -> list:
    """Sorts a list of book objects by publication year"""
    books_sorted = [book for book in sorted(books, key=lambda book: book.pub_year)]
    return books_sorted


def csv_to_books(csv: str) -> list[Book]:
    """Takes a string and turns it into list of Book objects"""
    books = []
    # Strip possible newline characters from start and end, then split
    csv = csv.split("\n")
    for line in csv:
        line = line.strip()
        line_split = line.split("/")
        try:
            books.append(
                Book(
                    line_split[BookFields.BOOK_NAME.value],
                    line_split[BookFields.BOOK_AUTHOR.value],
                    # we expect isbn and pub_year as int
                    int(line_split[BookFields.BOOK_ISBN.value]),
                    int(line_split[BookFields.BOOK_PUB_YEAR.value]),
                )
            )
        except IndexError as e:
            print("book db file is empty.\n", e)
    return books


def books_to_csv(books: list[Book]) -> str:
    """Constructs a string from book objects"""
    csv = ""
    for book in books:
        csv += f"{book.book_name}/{book.author_name}/{book.isbn}/{book.pub_year}\n"
    return csv
