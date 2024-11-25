import pytest
from src.vacancy import Vacancy, filter_by_salary


@pytest.fixture
def valid():
    """Фикстура для метода валидации класса Vacancy"""
    data = {
        "items": [
            {
                "name": "Тестировщик комфорта квартир",
                "area": {"name": "Воронеж"},
                "salary": {"from": 350000, "to": 450000, "currency": "RUR"},
                "apply_alternate_url": "https://hh.ru/applicant/vacancy_response?vacancyId=93353083",
                "responsibility": "Оценивать вид из окна."
            }
        ]
    }
    return Vacancy("Тестировщик комфорта квартир", "Воронеж", 350000, data)


@pytest.fixture
def city():
    """Фикстура для метода фильтрации по городу класса Vacancy"""
    data = {
        "items": [
            {
                "name": "Удаленный диспетчер чатов (в Яндекс)",
                "area": {"name": "Москва"},
                "salary": {"from": 20000, "to": None, "currency": "RUR"},
                "apply_alternate_url": "https://hh.ru/applicant/vacancy_response?vacancyId=92223756",
                "responsibility": "Обрабатывать входящие чаты."
            }
        ]
    }
    vacancy = Vacancy("Удаленный диспетчер чатов (в Яндекс)", "Москва", 20000, data)
    return vacancy.filter_city()


@pytest.fixture
def difference():
    """Фикстура для метода фильтрации по заработной плате класса Vacancy"""
    data = {
        "items": [
            {
                "name": "Удаленный диспетчер чатов (в Яндекс)",
                "area": {"name": "Москва"},
                "salary": {"from": 120000, "to": None, "currency": "RUR"},
                "apply_alternate_url": "https://hh.ru/applicant/vacancy_response?vacancyId=92223756",
                "responsibility": "Обрабатывать входящие чаты."
            }
        ]
    }
    test_vac = Vacancy("Удаленный диспетчер чатов (в Яндекс)", "Москва", 120000, data)
    city_vacancies = test_vac.filter_city()
    return filter_by_salary(120000, city_vacancies)


def test_valid(valid):
    """Тестирование метода валидации класса Vacancy"""
    assert valid.name == 'Тестировщик комфорта квартир'


def test_filter_city(city):
    """Тестирование метода фильтрации по городу класса Vacancy"""
    assert len(city) == 1
    assert city[0].name == 'Удаленный диспетчер чатов (в Яндекс)'


def test_difference(difference):
    """Тестирование фильтрации по зарплате"""
    assert len(difference) == 1
