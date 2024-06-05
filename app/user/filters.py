from django_filters.rest_framework import (
    FilterSet,
    ChoiceFilter,
)

from app.user.models import User
from utils import FriendshipStatus


class UserFilterSet(FilterSet):

    friend_status = ChoiceFilter(
        label='Friend Status',
        choices=FriendshipStatus.choices,
        field_name='friend_status'
    )

    class Meta:
        model = User
        fields = ["friend_status"]
