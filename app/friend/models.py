from django.db import models
from django.db.models import Q, Count
from django.utils.timezone import now

from utils import Helper, FriendChoice
from app.base.models import BaseModel



class FriendManager(models.Manager):

    def get_request(self, user1, user2):
        return self.filter(
            Q(sender=user1, receiver=user2) | Q(sender=user2, receiver=user1)
        ).first()

class Friend(BaseModel):
    sender = models.ForeignKey(
        "user.User", on_delete=models.CASCADE,related_name="sent_friend_requests"
    )
    receiver = models.ForeignKey(
        "user.User", on_delete=models.CASCADE, related_name="received_friend_requests"
    )
    status = models.CharField(
        max_length=6, choices=FriendChoice.choices, default=FriendChoice.SEND
    )

    class Meta:
        db_table = "friends"
        unique_together = ["sender", "receiver"]

    objects = FriendManager()
