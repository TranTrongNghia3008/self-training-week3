from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class EmailNotification(models.Model):
    recipient = models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.CharField(max_length=255)
    message = models.TextField()
    sent_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f'Notification to {self.recipient.email}'
