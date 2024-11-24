import unittest
from unittest.mock import patch, MagicMock
from src.vacancies_api import HH


class TestHH(unittest.TestCase):
    @patch('requests.get')
    def test_load_vacancies(self, mock_get):
        mock_response = MagicMock()
        mock_response.json.return_value = {
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
        mock_get.return_value = mock_response

        hh = HH()
        hh.load_vacancies('Тестировщик комфорта квартир')

        self.assertGreater(len(hh.vacancies), 0)
        self.assertEqual(hh.vacancies[0]['name'], 'Тестировщик комфорта квартир')
        self.assertEqual(hh.vacancies[0]['area']['name'], 'Воронеж')
        self.assertEqual(hh.vacancies[0]['employer']['name'], 'Специализированный застройщик BM GROUP')

        mock_get.assert_called_with(
            'https://api.hh.ru/vacancies',
            headers={'User-Agent': 'HH-User-Agent'},
            params={'text': 'Тестировщик комфорта квартир', 'page': 20, 'per_page': 100}
        )


if __name__ == '__main__':
    unittest.main()
