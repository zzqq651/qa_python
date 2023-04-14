# qa_python
Проверки:

Добавление книг - test_add_new_book

Проверить что нельзя дважды добавить книгу - test_you_cant_add_same_book_one_more_time

Недоступно выставление рейтинга книге не в списке - test_lack_of_rating_of_a_book_that_is_not_in_the_list

Нельзя поставить рейтинг < 1 - test_rating_less_one

Нельзя поставить рейтинг > 10 - test_rating_more_ten

Отсутствие рейгинга у книги, которая не добавлена - test_there_is_no_rating_for_a_non_existent_book

Добавление книги в избранное - test_add_to_favorites

Если книги в словаре нет, то и добаить в избранное её нельзя - test_book_no_favorites

Проверка удаления книги - test_deleting_a_book_from_favorites