import pytest


from main import BooksCollector

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_rating()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()
    def test_add_new_book(self, collector):
        collector.add_new_book("Интересная книга")
        assert len(collector.get_books_rating()) == 1, "Книга не добавилась"

    def test_you_cant_add_same_book_one_more_time(self, collector, White_Bim_Black_ear, Kolobok):
        assert len(collector.get_books_rating()) == 2, "Число книг не рано двум"

    def test_lack_of_rating_of_a_book_that_is_not_in_the_list(self, collector, White_Bim_Black_ear):
        collector.set_book_rating("Ни ной", 8)
        assert collector.get_books_rating() == {'Белый Бим чёрное ухо': 1}

    def test_rating_less_one(self, collector):
        collector.add_new_book("Любая книга")
        collector.set_book_rating("Любая книга", 0)
        assert collector.get_books_rating() != 1, "Доступен рейтинг < 1"

    def test_rating_more_ten(self, collector, White_Bim_Black_ear):
        collector.set_book_rating(White_Bim_Black_ear, 11)
        assert collector.get_books_rating() != 10, "Доступен рейтинг > 10"

    def test_there_is_no_rating_for_a_non_existent_book(self, collector):
        collector.add_new_book('Маша и медведь')
        collector.set_book_rating("Ни ной", 2)
        assert 'Ни ной' not in collector.get_list_of_favorites_books(), "Присвоен рейтинг книге, которая не добавлена"

    def test_add_to_favorites(self, collector):
        collector.add_new_book("Книга")
        collector.set_book_rating("Книга")
        assert len(collector.get_list_of_favorites_books()) == 1
        assert "Книга" in collector.get_list_of_favorites_books(), 'Не добавлена в избранное'

    def test_book_no_favorites(self, collector):
        collector.add_book_in_favorites('Три поросёнка')
        assert 'Три поросёнка' not in collector.favorites, "Добавление в избранное не существующей книги"

    def test_deleting_a_book_from_favorites(self, collector, White_Bim_Black_ear):
        collector.add_book_in_favorites(White_Bim_Black_ear)
        collector.delete_book_from_favorites(White_Bim_Black_ear)
        collector.get_list_of_favorites_books()
        assert len(collector.get_list_of_favorites_books()) == 0, "Книга из избранного не удалена"

    def test_getting_a_book_with_the_right_rating(self, collector, White_Bim_Black_ear, Kolobok, Ni_noy):
        collector.set_book_rating(White_Bim_Black_ear, 1)
        collector.set_book_rating(Kolobok, 6)
        collector.set_book_rating(Ni_noy, 10)
        assert len(collector.get_books_rating()) == 3, "Книги с не правильным рейтингом"

    def test_set_book_rating(self, collector, White_Bim_Black_ear):
        collector.add_new_book("Вини Пух")
        collector.set_book_rating("Вини Пух", 9)
        assert collector.books_rating.get("Вини Пух") == 9, "Рейтинг книги не соотвествует"