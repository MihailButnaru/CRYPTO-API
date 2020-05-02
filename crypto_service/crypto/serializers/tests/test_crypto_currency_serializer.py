from datetime import datetime, timedelta
from unittest import TestCase

from crypto.exceptions.api_exceptions import ValidationAPIError
from crypto.serializers import InputCryptoCurrencySerializer


class TestCryptoCurrencySerializers(TestCase):
    def setUp(self):
        self.input_data = {
            "crypto_currency": {
                "name": "BTC",
                "start_date": "2020-01-13",
                "end_date": datetime.utcnow().date(),
            }
        }

    def test_input_crypto_currency_it_can_serialize(self):
        """ Test ensures that the input data can be serialized
        successfully.
        """
        inst = InputCryptoCurrencySerializer(data=self.input_data)

        assert inst.is_valid()

        self.assertEqual(
            set(inst.validated_data["crypto_currency"]),
            set(self.input_data["crypto_currency"]),
        )

    def test_input_crypto_currency_start_date_greater_end_date(self):
        """ Test ensures that the start date is not greater than
        the end date, ValueError exception is raised. """

        self.input_data["crypto_currency"]["start_date"] = datetime.utcnow().date() + timedelta(days=1)

        inst = InputCryptoCurrencySerializer(data=self.input_data)

        with self.assertRaises(ValidationAPIError):
            inst.is_valid()

    def test_input_crypto_currency_end_date_less_start_date(self):
        """ Test ensures that the end date is not less than the
        start date, ValueError exception is raised."""

        self.input_data["crypto_currency"]["end_date"] = "2020-01-01"

        inst = InputCryptoCurrencySerializer(data=self.input_data)

        with self.assertRaises(ValidationAPIError):
            inst.is_valid()
