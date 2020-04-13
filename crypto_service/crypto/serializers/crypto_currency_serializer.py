from rest_framework import serializers


class CryptoCurrencySerializer(serializers.Serializer):
    name = serializers.CharField(max_length=50, default="BTC")
    start_date = serializers.DateField()
    end_date = serializers.DateField()


class InputCryptoCurrencySerializer(serializers.Serializer):
    crypto_currency = CryptoCurrencySerializer(many=False)


class OutputCryptoCurrencySerializer(serializers.Serializer):
    pass
