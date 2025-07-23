from rest_framework import serializers
from .models import EmailNotification

class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = ['id', 'recipient', 'subject', 'message', 'sent_at']