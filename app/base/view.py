from rest_framework.generics import GenericAPIView
from .mixins import (
    ListModelMixin,
    CreateModelMixin
)


class ListAPIView(ListModelMixin, GenericAPIView):
    pass


class CreateAPIView(CreateModelMixin, GenericAPIView):
    pass


class ListCreateAPIView(
    ListModelMixin, CreateModelMixin, GenericAPIView
):
    pass
