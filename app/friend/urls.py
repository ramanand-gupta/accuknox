from django.urls import path

from .views import (
    SendFriendRequestView,
    CancelFriendRequestView,
    AcceptFriendRequestView,
)


urlpatterns = [
    path('/send-request', SendFriendRequestView.as_view(), name='send-friend-request'),
    path('/cancel-request', CancelFriendRequestView.as_view(), name='cancel-friend-request'),
    path('/accept-request', AcceptFriendRequestView.as_view(), name='accept-friend-request'),
]
