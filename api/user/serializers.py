from datetime import datetime

from django.contrib.auth.models import models
from rest_framework import serializers

from .models import User
from permissions.utils import get_permissions


class UserSerializer(serializers.ModelSerializer):
    role = serializers.SerializerMethodField('get_role')
    role_display = serializers.SerializerMethodField('get_role_display')
    user_permissions = serializers.SerializerMethodField('get_user_permissions')
    is_superuser = models.BooleanField()

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'role', 'role_display', 'is_superuser')

        extra_kwargs = {'password': {'write_only': True}}

    def get_role(self, obj: User) -> str:
        return obj.role.name

    def get_role_display(self, obj: User) -> str:
        return obj.role.get_name_display()

    def get_user_permissions(self, obj: User) -> list:
        return get_permissions(obj)

    def update(self, instance: User, validated_data):
        instance.username = validated_data['username']
        instance.email = validated_data['email']

        if "role" in validated_data.keys():
            instance.role = validated_data['role']

        if 'password' in validated_data.keys():
            instance.set_password(validated_data['password'])

        today = datetime.now()
        instance.updated_at = today

        instance.save()
        return instance

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            role=validated_data['role']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user


class UserFrontendSerializer(serializers.ModelSerializer):
    role = serializers.SerializerMethodField('get_role')
    role_display = serializers.SerializerMethodField('get_role_display')
    is_superuser = serializers.BooleanField()

    class Meta:
        model = User
        exclude = ('password',)

    def get_role(self, obj: User) -> str:
        return obj.role.name

    def get_role_display(self, obj: User) -> str:
        return obj.role.get_name_display()

    def get_user_permissions(self, obj: User) -> list:
        return get_permissions(obj)
