from django.db import models


class Constant:
    
    API_MESSAGES = {
        100: "Congratulations! Registration successful.",
        101: "Welcome back! You have successfully logged in.",
        102: "Invalid credentials provided. Please try again.",
        103: "Logout successful. See you next time!",
        104: "User details.",
  
        105: "Friend request sent successfully!",
        106: "You've already sent a friend request to this user.",
        107: "Unable to send friend request, you've already received one from this user.",

        108: "No pending friend requests found. Start by initiating a new friend request.",  
        109: "Friend request canceled successfully.",
        110: "Cannot send a friend request to yourself!",

        111: "Friend request accepted!",
        112: "You are already friends with yourself!",
        113: "You are already friends.",
        114: "Please wait for the receiver to accept your friend request.",
        
        500: "Internal server error.",
        501: "The requested API endpoint is not valid.",
        502: "The provided data is not in a valid JSON format.",
        503: "The 'Content-Type' header should be set to 'application/json'.",
        504: "User authentication failed.",
        505: "The requested HTTP method is not allowed.",
        506: "Sorry, you are not authorized to perform this action.",
        507: "Invalid parameter passed.",
        508: "Your daily quota has been exhausted. Please try again later.",
        509: "User access token is expired or invalid.",
        510: "Request was throttled.",
        511: "User is not active."
    }



class FriendChoice(models.TextChoices):
    SEND = 'send', 'Send'
    ACCEPT = 'accept', 'Accept'


class FriendshipStatus(models.TextChoices):
    SENT = 'sent', 'Sent'
    RECEIVED = 'received', 'Received'
    FRIEND = 'friend', 'Friend'
    NO_FRIEND = 'no_friend', 'No Friend'
    ME = 'me', 'Me'
