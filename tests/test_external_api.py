import unittest
from unittest.mock import MagicMock, patch

from src.external_api import transaction_amount_in_rub


class TestTransactionAmount(unittest.TestCase):

    def test_rub(self):
        transaction = {
            "id": 441945886,
            "state": "EXECUTED",
            "date": "2019-08-26T10:50:58.294041",
            "operationAmount": {"amount": "31957.58", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод организации",
            "from": "Maestro 1596837868705199",
            "to": "Счет 64686473678894779589",
        }

        result = transaction_amount_in_rub(transaction)

        self.assertEqual(result, 31957.58)

    @patch("src.external_api.requests.request")
    def test_usd(self, mock_request):
        transaction = {
            "id": 41428829,
            "state": "EXECUTED",
            "date": "2019-07-03T18:35:29.512364",
            "operationAmount": {"amount": "8221.37", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод организации",
            "from": "MasterCard 7158300734726758",
            "to": "Счет 35383033474447895560",
        }

        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {"result": 661803.60384}

        mock_request.return_value = mock_response

        result = transaction_amount_in_rub(transaction)

        self.assertEqual(result, 661803.60384)

    @patch("src.external_api.requests.request")
    def test_api_error(self, mock_request):
        transaction = {
            "id": 41428829,
            "state": "EXECUTED",
            "date": "2019-07-03T18:35:29.512364",
            "operationAmount": {"amount": "8221.37", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод организации",
            "from": "MasterCard 7158300734726758",
            "to": "Счет 35383033474447895560",
        }

        mock_response = MagicMock()
        mock_response.status_code = 500

        mock_request.return_value = mock_response

        result = transaction_amount_in_rub(transaction)

        self.assertEqual(result, "Обращение к внешнему API не состоялось")
