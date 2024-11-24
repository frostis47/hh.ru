
import pytest
from src.vacancy import Vacancy, filter_by_salary


@pytest.fixture
def vacancies():
    """Фикстура для тестирования вакансий."""
    return [
        Vacancy(name="Тестировщик комфорта квартир", city="Воронеж", salary={"from": 350000}),
        Vacancy(name="Другой тестировщик", city="Москва", salary={"from": 300000})
    ]


def test_vacancy_creation(vacancies):
    """Тестирование создания вакансий."""
    assert len(vacancies) == 2
    assert vacancies[0].name == "Тестировщик комфорта квартир"


def test_salary_within_range(vacancies):
    """Тестирование диапазона зарплат."""
    assert vacancies[0].salary["from"] >= 300000


@pytest.fixture
def valid_vacancy():
    """Фикстура для метода валидации класса Vacancy."""
    return Vacancy("Тестировщик комфорта квартир", "Воронеж", salary={"from": 350000})


def test_valid(valid_vacancy):
    """Тестирование метода валидации класса Vacancy."""
    assert valid_vacancy.name == 'Тестировщик комфорта квартир'


@pytest.fixture
def city_vacancy():
    """Фикстура для метода фильтрации по городу класса Vacancy."""
    return Vacancy("Удаленный диспетчер чатов (в Яндекс)", "Москва", salary={"from": 20000})


def test_filter_city(city_vacancy):
    """Тестирование метода фильтрации по городу класса Vacancy."""
    assert city_vacancy.name == 'Удаленный диспетчер чатов (в Яндекс)'


@pytest.fixture
def salary_vacancies():
    """Фикстура для метода фильтрации по заработной плате класса Vacancy."""
    return [
        Vacancy("Удаленный диспетчер чатов (в Яндекс)", "Москва", salary={"from": 120000}),
        Vacancy("Другой диспетчер", "Москва", salary={"from": 80000})
    ]


def test_difference(salary_vacancies):
    """Тестирование фильтрации по зарплате."""
    filtered_vacancies = filter_by_salary(100000, salary_vacancies)
    assert len(filtered_vacancies) == 1
    assert filtered_vacancies[0].name == "Удаленный диспетчер чатов (в Яндекс)"
