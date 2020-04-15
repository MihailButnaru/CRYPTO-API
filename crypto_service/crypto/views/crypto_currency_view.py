from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

from crypto.routes import route_factory
from crypto.serializers import InputCryptoCurrencySerializer


class CryptoCurrencyViewSet(ViewSet):
    def create(self, request):
        """Viewset that is processing the
        crypto currency and displays the analysis.
        """
        serializer = InputCryptoCurrencySerializer(data=request.data)

        if not serializer.is_valid():
            return Response(status=status.HTTP_400_BAD_REQUEST, data=serializer.errors)

        response = route_factory.get_route(
            input_data=serializer.validated_data,
            crypto_currency_name=serializer.validated_data["crypto_currency"]["name"]
        )

        return Response(status=status.HTTP_201_CREATED, data=response.do_call_google([]))
