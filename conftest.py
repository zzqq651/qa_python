import pytest
from main import BooksCollector

@pytest.fixture()
def collector():
    collector = BooksCollector()
    return collector

@pytest.fixture()
def White_Bim_Black_ear(collector):
    collector.add_new_book('Белый Бим чёрное ухо')

@pytest.fixture()
def Kolobok(collector):
    collector.add_new_book('Колобок')

@pytest.fixture()
def Ni_noy(collector):
    collector.add_new_book('Ни ной')

