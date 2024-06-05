from rest_framework.throttling import UserRateThrottle


class SendFriendRequestRateThrottle(UserRateThrottle):
    scope = 'send_friend_request'
