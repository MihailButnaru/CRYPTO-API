from rest_framework.exceptions import APIException


class ServiceUnavailable(APIException):
    status_code = 500
    default_detail = "Service temporarily unavailalbe, try again later"
    default_code = "service_unavailable"


class PlatformAPIError(APIException):
    status_code = 500
    default_detail = "Service temporarily has an error, contact the administrator"
    default_code = "internal_server_error"


class AuthenticationFailed(APIException):
    status_code = 401
    default_detail = "Invalid credentials"


class ValidationAPIError(APIException):

    status_code = 400
    default_code = "bad_request"
