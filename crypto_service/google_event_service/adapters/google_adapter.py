# Copyright 2020
# All rights reserved. Mihail Butnaru
import logging
from django.conf import settings

from google.cloud import language

_logger = logging.getLogger(__name__)


def init_google_connection() -> language.LanguageServiceClient:
    """Initialize the google connection in order to get access
    to the google resources. """
    client = language.LanguageServiceClient.from_service_account_json(filename=settings.GOOGLE_AUTH_TOKEN)
    return client
