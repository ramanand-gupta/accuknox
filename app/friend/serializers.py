from rest_framework import serializers

from utils import Responder

from .models import Friend, FriendChoice


class SendFriendRequestSerializer(serializers.ModelSerializer):

    class Meta:
        model = Friend
        fields = ["receiver"]
        extra_kwargs = {
            "receiver": {"write_only": True}
        }
    
    def validate(self, attrs):
        sender = self.context['request'].user
        receiver = attrs['receiver']
        if sender == receiver:
            Responder.error(110)
        friend = Friend.objects.get_request(sender, attrs['receiver'])

        if not friend:
            return attrs
        elif friend.status == FriendChoice.ACCEPT:
            Responder.error(113)
        elif friend.sender == sender:
            Responder.error(106)
        else:
            Responder.error(107)


class CancelFriendRequestSerializer(serializers.ModelSerializer):

    class Meta:
        model = Friend
        fields = ["receiver"]
        extra_kwargs = {
            "receiver": {"write_only": True}
        }

    def validate(self, attrs):
        sender = self.context['request'].user
        friend = Friend.objects.get_request(sender, attrs['receiver'])
        if not friend:
            Responder.error(108)
        attrs["friend"] = friend
        return attrs
    
    def create(self, attrs):
        attrs["friend"].delete()
        return {}


class AcceptFriendRequestSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Friend
        fields = ["sender"]
        extra_kwargs = {
            "sender": {"write_only": True}
        }
    
    def validate(self, attrs):
        receiver = self.context['request'].user
        if receiver == attrs['sender']:
            Responder.error(112)
  
        friend = Friend.objects.get_request(receiver, attrs['sender'])
        if not friend:
            Responder.error(108)
        elif friend.status == FriendChoice.ACCEPT:
            Responder.error(113)
        elif friend.sender == receiver:
            Responder.error(114)
        attrs["friend"] = friend
        return attrs
    
    def create(Self, attrs):
        friend = attrs["friend"]
        friend.update({"status": FriendChoice.ACCEPT})
        return {}