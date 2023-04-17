from django.contrib.auth.models import User
from django.db import models
from item.models import Item

# Create your models here.
class Conversation(models.Model):
    item = models.ForeignKey(Item, related_name='conversations', on_delete=models.CASCADE)
    members = models.ManyToManyField(User, related_name='conversations')
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False)

    class Meta:
        ordering = ('-modified_at',)


class ConversationMessage(models.Model):
    conversation = models.ForeignKey(Conversation, related_name='messages', on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, related_name='created_messages', on_delete=models.CASCADE)
    is_delivered = models.BooleanField(default=False)
    is_read = models.BooleanField(default=False)


    def mark_as_read(self):
        self.is_read = True
        self.save()


    def mark_as_delivered(self):
        self.is_delivered = True
        self.save()
