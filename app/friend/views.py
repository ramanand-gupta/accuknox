from app.base.view import CreateAPIView
from utils import Responder

from .serializers import (
    SendFriendRequestSerializer,
    CancelFriendRequestSerializer,
    AcceptFriendRequestSerializer,
)
from .throttles import SendFriendRequestRateThrottle


class SendFriendRequestView(CreateAPIView):
    serializer_class = SendFriendRequestSerializer
    throttle_classes = [SendFriendRequestRateThrottle]
    
    def post(self, request, *args, **kwargs):
        data = self.create(request, *args, **kwargs)
        return Responder.success(105, data)

    def perform_create(self, serializer):
        serializer.save(sender=self.request.user)


class CancelFriendRequestView(CreateAPIView):
    serializer_class = CancelFriendRequestSerializer
    
    def post(self, request, *args, **kwargs):
        data = self.create(request, *args, **kwargs)
        return Responder.success(109, data)

    def perform_create(self, serializer):
        serializer.save(sender=self.request.user)


class AcceptFriendRequestView(CreateAPIView):
    serializer_class = AcceptFriendRequestSerializer
    
    def post(self, request, *args, **kwargs):
        data = self.create(request, *args, **kwargs)
        return Responder.success(111, data)

    def perform_create(self, serializer):
        serializer.save(receiver=self.request.user)