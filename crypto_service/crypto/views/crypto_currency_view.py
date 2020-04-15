import logging

from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

from crypto import JobProcessor
from crypto.serializers import (
    InputCryptoCurrencySerializer,
    OutputCryptoCurrencySerializer,
)

_logger = logging.getLogger(__name__)


class CryptoCurrencyViewSet(ViewSet):
    def create(self, request):
        """Viewset that is processing the
        crypto currency and displays the analysis.
        """
        serializer = InputCryptoCurrencySerializer(data=request.data)

        if not serializer.is_valid():
            return Response(status=status.HTTP_400_BAD_REQUEST, data=serializer.errors)

        response = JobProcessor.start_job_process(
            input_data=serializer.validated_data["crypto_currency"]
        )

        output_serializer = OutputCryptoCurrencySerializer(data=response, many=True)

        if not output_serializer.is_valid():
            _logger.error(f"Data does not match the object {output_serializer.errors}")
            return Response(status.HTTP_500_INTERNAL_SERVER_ERROR)

        return Response(
            status=status.HTTP_201_CREATED, data=output_serializer.validated_data
        )
