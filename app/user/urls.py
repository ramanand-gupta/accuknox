from django.urls import path

from .views import (
    UserRegisterView,
    UserLoginView,
    UserLogoutView,
    CurrentUserView,
    GetUserView,
)


urlpatterns = [
    path('/register', UserRegisterView.as_view(), name='user-register'),
    path('/login', UserLoginView.as_view(), name='user-login'),
    path('/logout', UserLogoutView.as_view(), name='user-logout'),
    path('/me', CurrentUserView.as_view(), name='current-user'),
    path('', GetUserView.as_view(), name='get-user'),
]
