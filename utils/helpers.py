import jwt

from django.conf import settings
from django.utils import timezone


class Helper:
    secret_key = settings.SECRET_KEY
    access_token_expiration_days = settings.ACCESS_TOKEN_EXPIRATION_DAYS
    
    @classmethod
    def decode_jwt_token(cls, token):
        return jwt.decode(
            token, cls.secret_key, algorithms=["HS256"]
        )

    @classmethod
    def encode_jwt_token(cls, payload):
        now = timezone.now()
        payload['iat'] = now
        payload['exp'] = now + timezone.timedelta(
            days=cls.access_token_expiration_days
        )
        return jwt.encode(
            payload, cls.secret_key, algorithm='HS256'
        )
