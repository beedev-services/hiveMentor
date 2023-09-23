from django.db import models
from userApp.models import *

class Chat(models.Model):
    title = models.CharField(max_length=255)
    adminUser = models.CharField(max_length=255)
    chatID = models.IntegerField()

class ChatMembers(models.Model):
    chatUser = models.ForeignKey(User, related_name='theChatUser', on_delete=CASCADE)
    chat = models.ForeignKey(Chat, related_name='theChat', on_delete=CASCADE)
