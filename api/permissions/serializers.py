from rest_framework import serializers

from permissions.models import UserRolePermission


class UserRolePermissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserRolePermission
        exclude = ("user_role",)
