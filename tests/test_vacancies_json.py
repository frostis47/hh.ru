from src.vacancies_json import HHVacancy
import json
import os

vacan = [{
    "name": "Middle Python Developer",
    "city": "Москва",
    "salary": {
        "from": 200000,
        "to": 0
    },
    "url": "https://hh.ru/vacancy/108969522",
    "description": "FastAPI, SQLAlchemy, Pydantic (v1/v2). Scrapy. Docker, Airflow, Celery, Redis. Postgres. Опыт "
                   "работы с Python от 2х..."
},
    {
        "name": "Python разработчик",
        "city": "Санкт-Петербург",
        "salary": {
            "from": 250000,
            "to": 300000
        },
        "url": "https://hh.ru/vacancy/108168771",
        "description": "Python 3. Опыт работы с фреймворком FastAPI и с асинхронным вызовами (Asyncpg, Asyncio ...). "
                       "Опыт работы с микросервисной архитектурой. Docker. PostgreSQL."
    }]


def test_save_vacancy():
    """Тестирование метода сохранения данных в файл"""
    test_1 = HHVacancy()
    test_1.safe_vacancy(vacan)


    with open('data/suitable_vacancies.json', 'r', encoding="utf-8") as file:
        saved_data = json.load(file)

    assert saved_data == vacan


def test_delete_vacancy():
    """Тестирование метода удаления из файла данных"""
    test_2 = HHVacancy()
    test_2.safe_vacancy(vacan)


    test_2.delete_vacancy('Санкт-Петербург')

    with open('data/suitable_vacancies.json', 'r', encoding="utf-8") as file:
        data = json.load(file)


    assert len(data) == 1
    assert data[0]['name'] == 'Middle Python Developer'


def test_vacancy_from_file():
    """Тестирование метода получения нужной вакансии"""
    test_3 = HHVacancy()
    test_3.safe_vacancy(vacan)

    result = test_3.vacancy_from_file('Москва')


    assert result == [vacan[0]]


def test_full_data_from_file():
    """Тестирование получения всех данных из файла"""
    test_4 = HHVacancy()
    test_4.safe_vacancy(vacan)

    assert test_4.full_data_from_file() == vacan

def teardown_module():
    try:
        os.remove('data/suitable_vacancies.json')
    except OSError:
        pass