from rest_framework.authentication import BaseAuthentication    

from utils import Responder, Helper
from app.user.models import User


class UserAuthentication(BaseAuthentication):
    
    def authenticate(self, request):
        token = request.headers.get("Authorization")
        if not token:
            return None

        try:
            payload = Helper.decode_jwt_token(token)
        except Exception:
            Responder.error(509)

        user = User.objects.get_by_pk(payload["uid"])
        if user is None:
            Responder.error(509)
        
        if not user.is_active:
            Responder.error(511)

        return (user, None)
