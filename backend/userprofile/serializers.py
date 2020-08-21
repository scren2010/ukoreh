from rest_framework import serializers

from backend.userprofile.models import Profile
from django.contrib.auth import get_user_model
User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'email', 'last_login', 'date_joined')
        extra_kwargs = {'last_login': {'read_only': True}, 'date_joined': {'read_only': True}}


class ProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Profile
        fields = ('user', 'id', 'picture', 'about', 'avatar')