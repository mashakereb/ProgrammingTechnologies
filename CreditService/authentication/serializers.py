from django.contrib.auth.models import User
from rest_framework.serializers import ModelSerializer, CharField

from .models import Profile


class ProfileSerializer(ModelSerializer):
    """
    DRF serializer for user's profile model
    """
    class Meta:
        model = Profile
        fields = '__all__'


class UserSerializer(ModelSerializer):
    """
    DRF serializer for User model
    """
    class Meta:
        model = User
        fields = (
            'username',
            'password',
            'first_name',
            'last_name',
        )

        password = CharField(write_only=True)

    def create(self, validated_data):
        user = super(UserSerializer, self).create(validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user

    def update(self, instance, validated_data):
        user = super(UserSerializer, self).update(instance, validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user
