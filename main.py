from src.vacancies_api import HH
from src.vacancy import Vacancy
from src.vacancies_json import HHVacancy
from src.utils import top_vacancy, filter_vacancy


def user_interaction():
    """Функция для взаимодействия с клиентом"""
    search_query = input("Введите поисковый запрос: ")
    hh = HH()
    city_search = input("Введите город для поиска вакансии: ")
    hh.load_vacancies(search_query)
    filter_words = input("Введите ключевые слова для фильтрации вакансий: ").split()

    # Обработка ввода желаемой зарплаты с проверкой на корректность
    while True:
        try:
            salary_threshold = int(input("Введите желаемую зарплату: "))
            break
        except ValueError:
            print("Пожалуйста, введите корректное целое число для зарплаты.")

    # Обработка ввода количества вакансий для вывода
    while True:
        try:
            top_n = int(input("Введите количество вакансий для вывода в топ N: "))
            break
        except ValueError:
            print("Пожалуйста, введите корректное целое число для количества вакансий.")

    # Начнём превращать каждый словарь от API в отдельную вакансию
    vacancy_instances = []
    for vacancy_info in hh.vacancies:
        name = vacancy_info['name']
        url = vacancy_info['alternate_url']
        requirements = vacancy_info['snippet'].get('requirement', '')
        city = vacancy_info['area']['name']

        # Обработка зарплаты
        salary = vacancy_info.get('salary')
        if salary is not None:
            salary_from = int(salary.get('from', 0) or 0)
            salary_to = int(salary.get('to', 0) or 0)
        else:
            salary_from = 0
            salary_to = 0

        # Создание экземпляра "Вакансии"
        vacancy = Vacancy(name, salary_from, salary_to, requirements, city, url)
        vacancy_instances.append(vacancy)

    # Фильтрация вакансий по городу и зарплате
    res_city = [vacancy for vacancy in vacancy_instances if vacancy.city == city_search]
    res_salary = [vacancy for vacancy in res_city if vacancy.salary_from >= salary_threshold]

    # Фильтрация по ключевым словам
    result_fil_words = filter_vacancy(res_salary, filter_words)

    # Сохранение вакансий в файл
    sd = HHVacancy()
    sd.safe_vacancy(result_fil_words)

    # Получение топ N вакансий
    result_of_top = top_vacancy(top_n, result_fil_words)

    # Удаление вакансий по ключевым словам
    del_vacancy = input("Требуется что-нибудь удалить из файла? 'Да,Нет': ")
    if del_vacancy.lower() == 'да':
        words_del = input('Введите ключевые слова для удаления вакансий (Название вакансии, город и т.п): ')
        sd.delete_vacancy(words_del)

    # Выборка данных для вывода
    fit_back = input("Требуется определенная выборка для вывода, или все данные из файла? 'Определенные,Все': ")
    if fit_back.lower() == 'определенные':
        words_sample = input("Введите ключевое слово для выборки данных (Город, название вакансии и т.п): ")
        sd.vacancy_from_file(words_sample)
    elif fit_back.lower() == "все":
        sd.full_data_from_file()

    return result_of_top


print(user_interaction())
