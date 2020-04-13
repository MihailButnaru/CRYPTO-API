from rest_framework import serializers


class CryptoCurrencySerializer(serializers.Serializer):
    """ Crypto currency serializer"""

    name = serializers.CharField(max_length=50, default="BTC")
    start_date = serializers.DateField()
    end_date = serializers.DateField()

    def validate(self, value):
        if value["start_date"] > value["end_date"]:
            raise ValueError("start date cannot be greater then end date")
        elif value["end_date"] < value["end_date"]:
            raise ValueError("end date cannot be less then start date")
        return value


class InputCryptoCurrencySerializer(serializers.Serializer):
    """ It serializes the input data from the user. """

    crypto_currency = CryptoCurrencySerializer(many=False)


class OutputCryptoCurrencySerializer(serializers.Serializer):
    pass
