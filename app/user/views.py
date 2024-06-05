from rest_framework.views import APIView
from rest_framework.permissions import AllowAny

from app.base.view import ListAPIView, CreateAPIView
from utils import Responder

from .serializers import (
    UserRegisterSerializer,
    UserLoginSerializer,
    UserDetailSerializer,
    CurrentUserSerializer,
)
from .models import User
from .filters import UserFilterSet


class UserRegisterView(CreateAPIView):
    permission_classes = [AllowAny]
    serializer_class = UserRegisterSerializer
    
    def post(self, request, *args, **kwargs):
        self.create(request, *args, **kwargs)
        return Responder.success(100)


class UserLoginView(CreateAPIView):
    permission_classes = [AllowAny]
    serializer_class = UserLoginSerializer

    def post(self, request, *args, **kwargs):
        data = self.create(request, *args, **kwargs)
        return Responder.success(101, data)


class UserLogoutView(APIView):
    def post(self, request):
        request.user.logout()
        return Responder.success(103)


class CurrentUserView(APIView):
    def get(self, request):
        serializer = CurrentUserSerializer(request.user)
        return Responder.success(104, serializer.data)
    

class GetUserView(ListAPIView):
    serializer_class = UserDetailSerializer
    search_fields = ["name", "email"]
    filterset_class = UserFilterSet
    
    def get_queryset(self):
        return User.objects.get_all(self.request.user)

    def get(self, request, *args, **kwargs):
        data = self.list(request, *args, **kwargs)
        return Responder.success(104, data)
