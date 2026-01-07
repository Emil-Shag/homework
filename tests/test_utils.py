import json
import unittest
from unittest.mock import MagicMock, mock_open, patch

with patch("logging.FileHandler", MagicMock()):
    from src.utils import get_transactions_from_file


class TestGetTransactions(unittest.TestCase):

    @patch(
        "src.utils.open",
        new_callable=mock_open,
        read_data=json.dumps(
            [
                {
                    "id": 1,
                    "state": "EXECUTED",
                    "date": "2023-01-01",
                    "description": "Перевод",
                    "from": "Счет 123",
                    "to": "Счет 456",
                    "operationAmount": {"amount": "1000", "currency": {"code": "RUB"}},
                }
            ]
        ),
    )
    def test_valid_json(self, mock_file):
        result = get_transactions_from_file("fake.json")
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0]["amount"], 1000.0)
        self.assertEqual(result[0]["currency"], "RUB")

    @patch("src.utils.logger")
    @patch("src.utils.open", side_effect=FileNotFoundError)
    def test_file_not_found(self, mock_open, mock_logger):
        result = get_transactions_from_file("missing.json")
        self.assertEqual(result, [])
