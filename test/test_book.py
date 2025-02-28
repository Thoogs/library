import pytest

from library.book import Book, sort_books

@pytest.fixture
def creare_test_list_of_books():
    return [
        Book("Moby Dick", "Herman Melville", 9781974305032, 1981),
        Book("Idiot", "Fyodor Dostoyevsky", 9780850670356, 1971)
    ]

def test_book():
    book = Book("Idiot", "Fyodor Dostoyevsky", 9780850670356, 1971)
    expected = "Book(book_name='Idiot', author_name='Fyodor Dostoyevsky', isbn=9780850670356, pub_year=1971)"
    assert str(book) == expected

def test_sort_books(creare_test_list_of_books):
    expected = [
        Book("Idiot", "Fyodor Dostoyevsky", 9780850670356, 1971),
        Book("Moby Dick", "Herman Melville", 9781974305032, 1981)
    ]
    assert sort_books(creare_test_list_of_books) == expected

