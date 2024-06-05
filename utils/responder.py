from rest_framework.response import Response

from conf.exceptions import ApiException
from .constant import Constant


class Responder:
    message = Constant.API_MESSAGES
    
    @classmethod
    def success(cls, code, data=None):
        return Response(
            {
                "status": True,
                "code": code,
                "message": cls.message[code],
                "data": {} if data is None else data,
            },
            200
        )
    
    @classmethod
    def _error(cls, code, error={}):
        if isinstance(error, str):
            message = error
            error = {}
        else:
            message = cls.message[code]
            
        return Response(
            {
                "status": False,
                "code": code,
                "message": message,
                "error": error
            },
            400
        )

    @staticmethod
    def error(code):
        raise ApiException(code)