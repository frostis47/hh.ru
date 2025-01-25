import pytest
import json
from src.vacancy import Vacancy

# Загружаем тестовые данные
with open('tests/data_tests.json', 'r', encoding="utf-8") as file:
    data = json.load(file)


@pytest.fixture
def valid():
    """Фикстура для создания валидной вакансии"""
    return Vacancy('Разработчик', 'Москва', 20000, data)


@pytest.fixture
def city(valid):
    """Фикстура для фильтрации вакансий по городу"""
    return valid.filter_city()


@pytest.fixture
def difference():
    """Фикстура для фильтрации вакансий по заработной плате"""
    test_vac = Vacancy('Разработчик', 'Москва', 120000, data)
    city_vacancies = test_vac.filter_city()

    return test_vac.filter_by_salary(city_vacancies, 120000)
