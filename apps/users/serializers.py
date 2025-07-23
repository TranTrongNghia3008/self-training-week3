from rest_framework import serializers
from .models import User  # use custom user model if you have one

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']
