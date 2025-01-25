import pytest
from src.vacancy import Vacancy

@pytest.fixture
def valid_vacancy():
    """Фикстура для создания валидной вакансии."""
    return Vacancy('Разработчик', 20000, 0, [], 'Москва', 'http://example.com')

def test_vacancy_creation(valid_vacancy):
    """Тестирование создания экземпляра Vacancy."""
    assert valid_vacancy.name == 'Разработчик'
    assert valid_vacancy.city == 'Москва'
    assert valid_vacancy.salary_from == 20000
    assert valid_vacancy.salary_to == 0
    assert valid_vacancy.url == 'http://example.com'

def test_filter_city(valid_vacancy):
    """Тестирование метода фильтрации по городу."""
    vacancies = [
        valid_vacancy,
        Vacancy('Менеджер', 30000, 0, [], 'Санкт-Петербург', 'http://example.com')
    ]
    filtered = Vacancy.filter_city(vacancies, 'Москва')
    assert len(filtered) == 1
    assert filtered[0].name == 'Разработчик'

def test_filter_by_salary():
    """Тестирование метода фильтрации по минимальной зарплате."""
    vacancies = [
        Vacancy('Разработчик', 120000, 0, [], 'Москва', 'http://example.com'),
        Vacancy('Менеджер', 80000, 0, [], 'Москва', 'http://example.com')
    ]
    filtered = Vacancy.filter_by_salary(vacancies, 100000)
    assert len(filtered) == 1
    assert filtered[0].name == 'Разработчик'

def test_to_json(valid_vacancy):
    """Тестирование метода to_json."""
    expected_json = {
        "name": 'Разработчик',
        "city": 'Москва',
        "salary": {
            "from": 20000,
            "to": 0
        },
        "url": 'http://example.com',
        "description": []
    }
    assert valid_vacancy.to_json() == expected_json
