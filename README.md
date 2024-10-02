# Финальный проект 
# Юнит тестирование
Цель финального проекта - покрыть тестами приложение BooksCollector. Оно позволяет установить жанр книг и добавить их в избранное 
Юнит-тестирование автоматизировано с использованием фикстур и параметризации.

Для запуска тестов используйте команду: pytest -v tests.py

# Фикстуры:

books_collection: создает экземпляр класса BooksCollector
my_books_collection: возвращает словарь типа {книга: жанр}

# Список сценариев тест-кейсов:

Позитивные кейсы:

test_add_new_book_add_two_books - проверка добавления двух книг
test_add_new_book_name_in_the_range - проверка на добавление книги с валидным названием (от 1 до 40 символов)
test_set_book_genre_to_existing_book - проверка на добавление жанра из genre для книги из books_genre
test_get_book_genre_by_name - проверка на вывод жанра книги по ее имени
test_get_books_with_specific_genre_by_genre - проверка на вывод книг по жанру
test_get_books_for_children - проверка на вывод детских книг
test_add_book_in_favorites_add_new_book_in_favorites_book - проверка на добавление книги в избранное
test_get_list_of_favorites_books - проверка на получение списка избранных книг
test_delete_book_from_favorites - проверка на удаление книги из избранного


Негативные кейсы:

test_add_new_book_the_book_already_added - негативная проверка на повторное добавление книги
test_add_new_book_name_out_of_range - негативная проверка на добавление книги с невалидной длинной названия (пусто, >=41 символ)
test_set_book_genre_to_not_existing_book - негативная проверка на добавление жанра из genre для книги не из books_genre
test_set_book_genre_to_not_existing_genre - негативная проверка на добавление жанра НЕ из genre для книги из books_genre
test_get_books_with_specific_genre_by_wrong_genre - негативная проверка на вывод книг по жанру НЕ из genre

