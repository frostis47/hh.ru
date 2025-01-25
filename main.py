from src.vacancies_api import HH
from src.vacancy import Vacancy
from src.vacancies_json import HHVacancy
from src.utils import top_vacancy, filter_vacancy


def user_interaction():
    """Функция для взаимодействия с клиентом"""
    search_query = input("Введите поисковый запрос: ")
    city_search = input("Введите город для поиска вакансии: ")

    hh = HH()
    hh.load_vacancies(search_query)

    filter_words = input("Введите ключевые слова для фильтрации вакансий: ").split()
    salary_threshold = get_valid_salary("Введите желаемую зарплату: ")
    top_n = get_valid_integer("Введите количество вакансий для вывода в топ N: ")

    vacancy_instances = Vacancy.cast_to_object_list(hh.vacancies)

    filtered_vacancies = filter_vacancies(vacancy_instances, city_search, salary_threshold, filter_words)

    if not filtered_vacancies:
        print("Вакансий с такими критериями не найдено.")
        return []

    save_vacancies(filtered_vacancies)

    result_of_top = top_vacancy(top_n, filtered_vacancies)

    delete_vacancies_if_needed(filtered_vacancies)

    display_vacancies()

    return result_of_top


def filter_vacancies(vacancy_instances, city_search, salary_threshold, filter_words):
    """Функция для фильтрации вакансий по городу, зарплате и ключевым словам."""
    res_city = [vacancy for vacancy in vacancy_instances if vacancy.city == city_search]
    res_salary = [vacancy for vacancy in res_city if vacancy.salary_from >= salary_threshold]
    return filter_vacancy(res_salary, filter_words)


def save_vacancies(vacancies):
    """Функция для сохранения отфильтрованных вакансий в файл."""
    sd = HHVacancy()
    sd.safe_vacancy(vacancies)


def delete_vacancies_if_needed(vacancies):
    """Функция для удаления вакансий по ключевым словам, если это необходимо."""
    if input("Требуется что-нибудь удалить из файла? 'Да,Нет': ").lower() == 'да':
        if not vacancies:
            print("Нет вакансий для удаления.")
        else:
            words_del = input('Введите ключевые слова для удаления вакансий (Название вакансии, город и т.п): ')
            sd = HHVacancy()
            sd.delete_vacancy(words_del)


def display_vacancies():
    """Функция для выбора и отображения вакансий."""
    fit_back = input("Требуется определенная выборка для вывода, или все данные из файла? 'Определенные,Все': ")
    sd = HHVacancy()
    if fit_back.lower() == 'определенные':
        words_sample = input("Введите ключевое слово для выборки данных (Город, название вакансии и т.п): ")
        vacancies = sd.vacancy_from_file(words_sample)
        print(vacancies)
    elif fit_back.lower() == "все":
        vacancies = sd.full_data_from_file()
        print(vacancies)


def get_valid_salary(prompt):
    """Функция для получения корректного ввода желаемой зарплаты"""
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Пожалуйста, введите корректное целое число для зарплаты.")


def get_valid_integer(prompt):
    """Функция для получения корректного ввода целого числа"""
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Пожалуйста, введите корректное целое число.")


if __name__ == "__main__":
    print(user_interaction())



