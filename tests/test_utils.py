import unittest
from unittest.mock import mock_open, patch

from src.utils import get_transactions_from_file


class TestGetTransactions(unittest.TestCase):

    @patch(
        "builtins.open", new_callable=mock_open, read_data='[{"id": 123, "currency": {"code": "RUB", "amount": 1000}}]'
    )
    def test_valid_json_list(self, mock_file):
        result = get_transactions_from_file("fake.json")
        self.assertEqual(len(result), 1)

    @patch(
        "builtins.open", new_callable=mock_open, read_data='{"id": 123, "currency": {"code": "RUB", "amount": 1000}}'
    )
    def test_json_not_list(self, mock_file):
        result = get_transactions_from_file("fake.json")
        self.assertEqual(result, [])

    @patch(
        "builtins.open", new_callable=mock_open, read_data='{"id": 123, "currency": {"code": "RUB", "amount": 1000}}'
    )
    def test_invalid_json(self, mock_file):
        result = get_transactions_from_file("fake.json")
        self.assertEqual(result, [])

    @patch("builtins.open", side_effect=FileNotFoundError)
    def test_file_not_found(self, mock_file):
        result = get_transactions_from_file("missing.json")
        self.assertEqual(result, [])
