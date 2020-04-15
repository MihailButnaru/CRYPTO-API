from datetime import datetime

from rest_framework import serializers

from crypto.exceptions.api_exceptions import ValidationAPIError


class CryptoCurrencySerializer(serializers.Serializer):
    """ Crypto currency serializer"""

    name = serializers.ChoiceField(default="BTC", choices=["BTC"])
    start_date = serializers.DateField()
    end_date = serializers.DateField()

    def validate(self, value):
        if value["start_date"] > value["end_date"]:
            raise ValidationAPIError(
                detail=f"start date {value['start_date']} cannot be greater then end date {value['end_date']}"
            )
        elif value["end_date"] != datetime.utcnow().date():
            raise ValidationAPIError(
                detail=f"{value['end_date']} must be today: {datetime.utcnow().date()}"
            )
        return value


class InputCryptoCurrencySerializer(serializers.Serializer):
    """ It serializes the input data from the user. """

    crypto_currency = CryptoCurrencySerializer(many=False)


class OutputCryptoCurrencySerializer(serializers.Serializer):
    sentence = serializers.CharField(max_length=500, required=False, allow_null=True)
    polarity = serializers.FloatField()
    subjectivity = serializers.FloatField()
