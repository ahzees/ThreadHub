from django.db import models
from authentication.models import CustomUser

class Thread(models.Model):
    name = models.CharField("name of thread", max_length=555, null=False, blank=False, unique=True)
    members = models.ManyToManyField(CustomUser, related_name="threads")
    messages = models.ForeignKey("Messages", on_delete=models.DO_NOTHING, null=True, related_name="thread")

class Messages(models.Model):
    user = models.ForeignKey(Thread, on_delete=models.CASCADE, related_name="thread_user_messages", null=True)
    content = models.TextField("content of message", null=False, blank=False, default="Hello")
    # Add other fields as needed
