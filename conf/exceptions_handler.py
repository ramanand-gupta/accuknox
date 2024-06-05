import traceback

from django.conf import settings
from django.urls.exceptions import Resolver404
from rest_framework.decorators import api_view
from rest_framework.exceptions import (
    MethodNotAllowed,
    ParseError,
    UnsupportedMediaType,
    NotAuthenticated,
    AuthenticationFailed,
    PermissionDenied,
    ValidationError as DRFValidationError,
    Throttled,
)

from utils import Responder, Constant
from .exceptions import ApiException


def exception_handler(exception, context):
    exeption_mapper = {
        Resolver404: 501,
        ParseError: 502,
        UnsupportedMediaType: 503,
        NotAuthenticated: 504,
        AuthenticationFailed: 504,
        MethodNotAllowed: 505,
        PermissionDenied: 506,
        DRFValidationError: 507,
        ApiException: lambda exception: exception.code,
        Throttled: 510,
    }

    response_code = exeption_mapper.get(type(exception), 500)
    if callable(response_code):
        response_code = response_code(exception)

    if response_code == 500 and settings.DEBUG:
        raise exception
    
    error = getattr(exception, "detail", {})
    return Responder._error(response_code, error)


@api_view(("GET",))
def handler404(request, exception):
    return Responder.error(501, status=False)
