"""Contains code required to manipulate the csv db"""

from typing import TextIO


def read_header(db_file: TextIO) -> str:
    """Returns cursor to start and reads the header line and returns it"""
    # Move cursor to start, as we never know it's location
    db_file.seek(0)
    # Read headers
    header = db_file.readline()
    return header


def write_header(db_file: TextIO, header: str):
    """Opens a new write session on db file, overwriting it, and writes header line"""
    # Move cursor to start
    db_file.seek(0)
    # Write header
    db_file.write(header)


def read_data(db_file: TextIO) -> str:
    """Reads data lines from file and yield it as a string.
    We expect that read_header has been called before read_data"""
    books_csv = ""
    for row in db_file:
        books_csv += row
    return books_csv


def write_data(db_file: TextIO, book_data: str):
    """Writes the book data from a string into the db_file"""
    db_file.write(book_data)
