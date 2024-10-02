import pytest
from main import BooksCollector


class TestBooksCollector:
    # Позитивные проверки

    def test_add_new_book_add_two_books(self):
        collector = BooksCollector()
        collector.add_new_book('Шерлок')
        collector.add_new_book('Маленькие женщины')
        assert collector.get_books_genre() == {'Шерлок': '',
                                               'Маленькие женщины': ''}

    @pytest.mark.parametrize('name', ['Песнь льда и пламени',
                                      'Песнь льда и пламени Джорджа Мартина Мл.',
                                      'Я'])
    def test_add_new_book_name_in_the_range(self, name, books_collection):
        books_collection.add_new_book(name)
        assert name in books_collection.get_books_genre()

    def test_set_book_genre_to_existing_book(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение')
        collector.set_book_genre('Гордость и предубеждение', 'Фантастика')
        assert collector.get_books_genre() == {'Гордость и предубеждение': 'Фантастика'}

    @pytest.mark.parametrize('name, genre', [('Шерлок', 'Детективы'),
                                             ('Оно', 'Ужасы')])
    def test_get_book_genre_by_name(self, name, genre):
        collector = BooksCollector()
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)
        assert collector.get_book_genre(name) == genre

    @pytest.mark.parametrize('name, genre', [('Шерлок', 'Детективы'),
                                             ('Оно', 'Ужасы')])
    def test_get_books_with_specific_genre_by_genre(self, name, genre):
        collector = BooksCollector()
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)
        assert collector.get_books_with_specific_genre(genre) == [name]

    def test_get_books_for_children(self, my_books_collection):
        assert len(
            my_books_collection.get_books_for_children()) == 3 and my_books_collection.get_books_for_children() == [
                   'Я - легенда', 'Маленький принц', 'Горе от ума']

    def test_add_book_in_favorites_add_new_book_in_favorites_book(self, my_books_collection):
        my_books_collection.add_book_in_favorites('Я - легенда')
        assert 'Я - легенда' in my_books_collection.get_list_of_favorites_books() and len(
            my_books_collection.get_list_of_favorites_books()) == 1

    def test_get_list_of_favorites_books(self, my_books_collection):
        my_books_collection.add_book_in_favorites('Я - легенда')
        my_books_collection.add_book_in_favorites('Маленький принц')
        assert my_books_collection.get_list_of_favorites_books() == ['Я - легенда', 'Маленький принц']

    def test_delete_book_from_favorites(self, my_books_collection):
        my_books_collection.add_book_in_favorites('Я - легенда')
        my_books_collection.delete_book_from_favorites('Я - легенда')
        assert len(my_books_collection.get_list_of_favorites_books()) == 0

    # Негативные проверки

    def test_add_new_book_the_book_already_added(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Гордость и предубеждение и зомби')
        assert collector.get_books_genre() == {'Гордость и предубеждение и зомби': ''}

    @pytest.mark.parametrize('name', ['',
                                      'Странная история доктора Джекила и мистера Хайда',
                                      'Странная история доктора Джекила и мистер'])
    def test_add_new_book_name_out_of_range(self, name, books_collection):
        books_collection.add_new_book(name)
        assert len(books_collection.get_books_genre()) == 0

    def test_set_book_genre_to_not_existing_book(self):
        collector = BooksCollector()
        collector.set_book_genre('Гордость и предубеждение', 'Фантастика')
        assert collector.get_books_genre() == {}

    def test_set_book_genre_to_not_existing_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Властелин колец')
        collector.set_book_genre('Властелин колец', 'Фэнтези')
        assert collector.get_books_genre() == {'Властелин колец': ''}

    def test_get_books_with_specific_genre_by_wrong_genre(self, my_books_collection):
        assert len(my_books_collection.get_books_with_specific_genre('Фэнтези')) == 0
