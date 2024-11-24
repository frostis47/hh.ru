import unittest


class TestVacancies(unittest.TestCase):
    def setUp(self):
        self.vacancies = {
            'items': [
                {
                    'name': 'Тестировщик комфорта квартир',
                    'salary': {'from': 350000, 'to': 450000, 'currency': 'RUR'},
                    'area': {'name': 'Воронеж'},
                    'employer': {'name': 'Специализированный застройщик BM GROUP'},
                    'apply_alternate_url': 'https://hh.ru/applicant/vacancy_response?vacancyId=93353083'
                },
                {
                    'name': 'Удаленный диспетчер чатов (в Яндекс)',
                    'salary': {'from': 20000, 'to': 30000, 'currency': 'RUR'},
                    'area': {'name': 'Москва'},
                    'employer': {'name': 'Яндекс'},
                    'apply_alternate_url': 'https://hh.ru/applicant/vacancy_response?vacancyId=92223756'
                }
            ]
        }

    def test_vacancy_count(self):
        self.assertEqual(len(self.vacancies['items']), 2)

    def test_first_vacancy_name(self):
        self.assertEqual(self.vacancies['items'][0]['name'], 'Тестировщик комфорта квартир')

    def test_first_vacancy_salary(self):
        self.assertEqual(self.vacancies['items'][0]['salary']['from'], 350000)
        self.assertEqual(self.vacancies['items'][0]['salary']['to'], 450000)
        self.assertEqual(self.vacancies['items'][0]['salary']['currency'], 'RUR')

    def test_first_vacancy_area(self):
        self.assertEqual(self.vacancies['items'][0]['area']['name'], 'Воронеж')

    def test_first_vacancy_employer(self):
        self.assertEqual(self.vacancies['items'][0]['employer']['name'], 'Специализированный застройщик BM GROUP')

    def test_second_vacancy_name(self):
        self.assertEqual(self.vacancies['items'][1]['name'], 'Удаленный диспетчер чатов (в Яндекс)')

    def test_second_vacancy_salary(self):
        self.assertEqual(self.vacancies['items'][1]['salary']['from'], 20000)
        self.assertEqual(self.vacancies['items'][1]['salary']['to'], 30000)
        self.assertEqual(self.vacancies['items'][1]['salary']['currency'], 'RUR')

    def test_second_vacancy_area(self):
        self.assertEqual(self.vacancies['items'][1]['area']['name'], 'Москва')

    def test_second_vacancy_employer(self):
        self.assertEqual(self.vacancies['items'][1]['employer']['name'], 'Яндекс')

    def test_apply_url(self):
        self.assertEqual(self.vacancies['items'][0]['apply_alternate_url'],
                         'https://hh.ru/applicant/vacancy_response?vacancyId=93353083')
        self.assertEqual(self.vacancies['items'][1]['apply_alternate_url'],
                         'https://hh.ru/applicant/vacancy_response?vacancyId=92223756')


if __name__ == '__main__':
    unittest.main()
