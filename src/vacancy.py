class Vacancy:
    def __init__(self, name, salary_from, salary_to, requirements, city, url):
        self.name = name
        self.salary_from = salary_from
        self.salary_to = salary_to
        self.requirements = requirements
        self.city = city
        self.url = url

    @classmethod
    def cast_to_object_list(cls, vacancies):
        """Метод для преобразования списка словарей в список экземпляров класса Vacancy."""
        vacancy_instances = []
        for vacancy_info in vacancies:
            try:
                name = vacancy_info['name']
                salary_info = vacancy_info.get('salary', {})
                salary_from = salary_info.get('from', 0) if salary_info else 0
                salary_to = salary_info.get('to', 0) if salary_info else 0
                requirements = vacancy_info.get('requirements', [])
                city = vacancy_info['area']['name']
                url = vacancy_info['alternate_url']

                vacancy = cls(name, salary_from, salary_to, requirements, city, url)
                vacancy_instances.append(vacancy)
            except KeyError as e:
                print(f"Пропущена вакансия из-за отсутствия ключа: {e} в данных: {vacancy_info}")

        return vacancy_instances

    def __repr__(self):
        """Метод для представления экземпляра вакансии в виде строки."""
        return (f"Vacancy(name={self.name}, salary_from={self.salary_from}, "
                f"salary_to={self.salary_to}, requirements={self.requirements}, "
                f"city={self.city}, url={self.url})")

    def to_json(self):
        """Метод для преобразования экземпляра вакансии в словарь."""
        return {
            "name": self.name,
            "city": self.city,
            "salary": {
                "from": self.salary_from,
                "to": self.salary_to
            },
            "url": self.url,
            "description": self.requirements
        }

    @staticmethod
    def reform_file(data_hh):
        """Метод для обработки JSON-ответа от сайта HH.ru."""
        result = []
        for i in data_hh:
            salary_info = i.get("salary", {})
            salary_from = salary_info.get("from", 0)
            salary_to = salary_info.get("to", 0)
            currency = salary_info.get("currency")

            if currency == 'RUR':
                result.append({
                    "name": i["name"],
                    "city": i["area"]["name"],
                    "salary": {"from": salary_from, "to": salary_to},
                    "url": i["alternate_url"],
                    "description": i["snippet"]["requirement"]
                })
        return result

    @staticmethod
    def filter_city(vacancies, city):
        """Метод фильтрации списка вакансий по нужному городу."""
        return [vac for vac in vacancies if vac.city == city]

    @staticmethod
    def filter_by_salary(vacancies, min_salary):
        """Метод фильтрации списка вакансий по минимальной зарплате."""
        return [vac for vac in vacancies if vac.salary_from >= min_salary]

