"""TUI functions as our main interface to the program"""

import argparse
from os import path, name, system

from library.book import Book, sort_books, books_to_csv, csv_to_books
from library.db_handler import write_data, write_header, read_data, read_header

BOOK_NAME_LEN = 35
BOOK_AUTHOR_LEN = 35
BOOK_ISBN_LEN = 13
BOOK_PUB_YEAR_LEN = 4
ROW_LENGTH = 98


def clear():
    # if we are on windows
    if name == "nt":
        _ = system("cls")

    # If we are on linux / mac
    else:
        _ = system("clear")


def print_main_menu() -> str:
    """Prints the main menu for the application and returns user input"""
    header = """
    ####################################################
    # Library terminal app by Teemu 'Thoogs' Mahlamäki #
    ####################################################
    """
    print(header)
    print("Select one of the following operations:")
    print("[1]: Add new book to db")
    print("[2]: Print current database")
    print("[q]: Exit\n")
    user_choice = input("Your choice: ")
    return user_choice


def print_header(header: str):
    """Takes the header string and assembles the header line."""
    if len(header) == 0:
        header = "book/author/ISBN/year"
    header_split = header.strip().split("/")
    # assemble header
    # This could be done more cleanly by assigning each header column one at a time
    # and then concatenating them together.
    header_str = f"{header_split[0]:{BOOK_NAME_LEN}} | {header_split[1]:{BOOK_AUTHOR_LEN}} | {header_split[2]:{BOOK_ISBN_LEN}} | {header_split[3]:{BOOK_PUB_YEAR_LEN}} |\n"
    header_len = len(header_str)
    # Print the headers
    print(header_str, end="")
    # Print row separator
    print("-" * header_len)


def print_data(books: list[Book]):
    """Prints the stored data from book objects and formats the output into
    a table."""
    for book in books:
        # This could be done more cleanly by assigning each header column one at a time
        # and then concatenating them together.
        data_row = f"{book.book_name:{BOOK_NAME_LEN}} | {book.author_name:{BOOK_AUTHOR_LEN}} | {book.isbn:{BOOK_ISBN_LEN}} | {book.pub_year:{BOOK_PUB_YEAR_LEN}}"
        print(data_row)
        print("-" * ROW_LENGTH)


def add_book_to_db(books: list[Book], db_file: str, header: str) -> list[Book]:
    """Queries data from user and inserts it into our db file."""
    # Get user input
    print("Add book to db\n")
    book_name = input("Book name: ")
    book_author = input("Book author: ")
    book_isbn = input("Book ISBN: ")
    book_pub_year = input("Book publishing year: ")
    # clear screen here
    clear()
    # Confirm user data and chose if we write it
    print(f"""Data you entered: 
    Book name: {book_name}
    Book author: {book_author}
    Book ISBN: {book_isbn}
    Book publication year: {book_pub_year}\n
    """)
    write_to_db = input("Write changes to db? y/n :")

    if write_to_db.lower() == "y":
        # Add new book to our db
        books.append(Book(book_name, book_author, int(book_isbn), int(book_pub_year)))
        # Sort the db
        books = sort_books(books)
        # Add our new book to the file

        # We open in write mode to make sure we get no errors in the file if lines
        # have changed places
        with open(db_file, "w") as db_write:
            write_header(db_write, header)
            books_csv = books_to_csv(books)
            write_data(db_write, books_csv)

    # if we don't write, we just return the db without the new book
    return books


def main():
    # parse our arguments
    parser = argparse.ArgumentParser()
    parser.add_argument("db_file", help="csv file used as our database")
    args = parser.parse_args()
    db_file = args.db_file

    # Make sure the file exists, if not then create it.
    if not path.isfile(db_file):
        print("File does not exist, create new file")
        with open(db_file, "x+") as book_db:
            book_db.write("Book/Author/ISBN/Year\n")

    # Open the db file and start main loop
    try:
        while True:
            with open(db_file, "r") as book_db:
                # read our header and data
                header = read_header(book_db)
                books_csv = read_data(book_db)
                # Convert the csv to list of objects
                books = csv_to_books(books_csv)
                # See what the user wants to do
                user_choice = print_main_menu()
                match user_choice.lower():
                    case "1":
                        add_book_to_db(books, db_file, header)
                        clear()
                    case "2":
                        print_header(header)
                        print_data(books)
                        input("press Enter to continue..")
                        clear()

                    case "q":
                        return
                    case _:
                        clear()
                        print("Invalid option.")

    except Exception as e:
        print("Cannot open or edit file.", e)


if __name__ == "__main__":
    main()
