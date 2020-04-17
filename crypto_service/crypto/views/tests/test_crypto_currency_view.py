import unittest
from unittest import TestCase
from unittest.mock import patch
from datetime import date, datetime
from django.test import RequestFactory

from rest_framework import status
from crypto.views import CryptoCurrencyViewSet


class TestCryptoCurrencyViewSet(TestCase):
    def setUp(self) -> None:
        self.input_data = {
            "crypto_currency": {
                "name": "BTC",
                "start_date": date(2020, 4, 13),
                "end_date": datetime.utcnow().date(),
            }
        }
        self.output_data = [
            {
                "sentence": ": New York Power Plant Sells Bitcoin Hashpower to Institutional Investors",
                "polarity": 0.13636363636363635,
                "subjectivity": 0.45454545454545453,
            }
        ]
        self.factory = RequestFactory()

    @unittest.skip
    @patch("crypto.job_process_event.JobProcessor.start_job_process")
    def test_create(self, mock_start_job_process):
        mock_start_job_process.return_value = self.output_data

        request = self.factory.post(
            path="/v0/crypto_analysis/",
            data=self.input_data,
            content_type="application/json",
        )
        response = CryptoCurrencyViewSet.as_view({"post": "create"})(request)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data, mock_start_job_process.return_value)
