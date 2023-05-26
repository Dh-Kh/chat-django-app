from django.db import models
class MessageHistory(models.Model):
    message = models.CharField(max_length=200)
    chat_name = models.ForeignKey("ChatNameHistory", on_delete = models.CASCADE)

class ChatNameHistory(models.Model):
    chat_name = models.CharField(max_length=200,unique=True)
    chat_creator = models.CharField(max_length=200, null=True)

    

    