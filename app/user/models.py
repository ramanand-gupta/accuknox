from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin
)
from django.db import models
from django.db.models import Q, Count, Case, When, Value
from django.utils.timezone import now

from utils import Helper, FriendshipStatus
from app.base.models import BaseModel
from app.friend.models import FriendChoice



class UserManager(BaseUserManager):

    def _create_user(self, email, password, **kwargs):
        email = self.normalize_email(email)
        user = self.model(email=email, **kwargs)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **kwargs):
        kwargs.setdefault("is_staff", True)
        kwargs.setdefault("is_superuser", True)
        self._create_user(email, password, **kwargs)

    def get_by_pk(self, pk):
        return self.filter(pk=pk).first()
    
    def get_by_email(self, email):
        return self.filter(email=email).first()

    def get_by_credential(self, email, password):
        user = self.get_by_email(email)
        return (
            user if user is not None and user.check_password(password)
            else None
        )

    def get_all(self, user):
        is_self = Q(id=user.id)
        sent_request = Q(
            received_friend_requests__sender=user,
            received_friend_requests__status=FriendChoice.SEND
        )
        received_request = Q(
            sent_friend_requests__receiver=user,
            sent_friend_requests__status=FriendChoice.SEND
        )
        sent_accepted = Q(
            sent_friend_requests__receiver=user,
            sent_friend_requests__status=FriendChoice.ACCEPT
        )
        received_accepted = Q(
            received_friend_requests__sender=user,
            received_friend_requests__status=FriendChoice.ACCEPT
        )

        is_friend = sent_accepted | received_accepted

        friend_status_case = Case(
            When(is_self, then=Value(FriendshipStatus.ME)),
            When(sent_request, then=Value(FriendshipStatus.SENT)),
            When(received_request, then=Value(FriendshipStatus.RECEIVED)),
            When(is_friend, then=Value(FriendshipStatus.FRIEND)),
            default=Value(FriendshipStatus.NO_FRIEND)
        )

        return self.annotate(friend_status=friend_status_case).distinct()


class User(BaseModel, AbstractBaseUser, PermissionsMixin):
    name = models.CharField(max_length=120)
    email = models.EmailField(unique=True, max_length=120)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        db_table = "users"
        ordering = ["-pk"]

    objects = UserManager()

    def create_access_token(self):
        payload = {"uid": self.id}
        return Helper.encode_jwt_token(payload)

    def login(self):
        return {
            "id": self.id,
            'name': self.name,
            "email": self.email,
            "access_token": self.create_access_token()
        }

    def logout(self):
        pass
