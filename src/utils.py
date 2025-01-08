def top_vacancy(number, my_list):
    """Функция вывода Топ-n вакансий для пользователя"""
    if number == "":
        return my_list
    else:
        return my_list[0:int(number)]


def filter_vacancy(vacancies, filter_words):
    """Фильтрует вакансии по ключевым словам."""
    filtered_vacancies = []

    for vacancy in vacancies:
        description = vacancy.requirements
        name = vacancy.name

        if any(word in description for word in filter_words) or any(word in name for word in filter_words):
            filtered_vacancies.append(vacancy)

    return filtered_vacancies
