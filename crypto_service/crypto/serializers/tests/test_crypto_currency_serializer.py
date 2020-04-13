from unittest import TestCase

from crypto.serializers import (
    InputCryptoCurrencySerializer
)


class TestCryptoCurrencySerializers(TestCase):
    def setUp(self):
        self.input_data = {
            "crypto_currency": {
                "name": "BTC",
                "start_date": "2020-01-13",
                "end_date": "2020-04-13"
            }
        }

    def test_input_crypto_currency_it_can_serialize(self):
        inst = InputCryptoCurrencySerializer(data=self.input_data)

        assert inst.is_valid()

        self.assertEqual(set(inst.validated_data["crypto_currency"]),
                         set(self.input_data["crypto_currency"]))
