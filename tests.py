import pytest

book_test = 'Белый Бим чёрное ухо'
any_book = 'Колобок'
books_with_ratings = {
    book_test: 5,
    any_book: 10,
    'Ни ной': 7
}

class TestBooksCollector:

    def test_books_rating_type_is_dictionary(self, collector):
        assert collector.get_books_rating() == {}, 'Рейтинг книг не словарь'

    def test_favorites_type_is_list(self, collector):
        assert collector.get_list_of_favorites_books() == [], 'Список избранных книг не является списком'

    def test_add_books(self, collector):
        collector.add_new_book(book_test)
        collector.add_new_book(any_book)
        assert len(collector.get_books_rating()) == 2, 'Книги не добавлены'

    def test_add_same_books(self, collector):
        collector.add_new_book(book_test)
        collector.add_new_book(book_test)
        assert len(collector.get_books_rating()) == 1, 'Книги добавлены'
    def test_add_rating_to_nonexistent_book_rating_is_none(self, collector):
        collector.set_book_rating(book_test, 10)
        assert collector.get_book_rating(book_test) is None, 'Добавлен рейтинг несуществующей книги'

    def test_get_book_rating_get_nonexistent_book_rating(self, collector):
        assert collector.get_book_rating(book_test) is None, 'Рейтинг несуществующей книги'

    def test_add_book_in_favorites_add_new_book_book_in_favorites(self, collector):
        collector.add_new_book(book_test)
        collector.add_book_in_favorites(book_test)
        assert book_test in collector.get_list_of_favorites_books(), 'Книга не добавлена в избранное'

    def test_add_book_with_rating_more_than_nine(self, collector):
        for book, book_rating in books_with_ratings.items():
            collector.add_new_book(book)
            collector.set_book_rating(book, book_rating)
        assert len(collector.get_books_with_specific_rating(9)) == 1, 'Нет книги с рейтингом больше 9'

    def test_add_and_remov_a_book_from_favorites(self, collector):
        collector.add_new_book(book_test)
        collector.add_book_in_favorites(book_test)
        collector.delete_book_from_favorites(book_test)
        assert len(collector.get_list_of_favorites_books()) == 0, 'Книга не удалена'
