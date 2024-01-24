from .models import UserRolePermission
from .serializers import UserRolePermissionSerializer

from users.models import User


def has_permission(permission, user: User):
    if user.is_superuser:
        return True
    role = user.role
    has_role = UserRolePermission.objects.filter(user_role=role, permission=permission).exists()
    return has_role


def get_permissions(user: User):
    role = user.role
    permissions = UserRolePermission.objects.filter(user_role=role)
    serializer = UserRolePermissionSerializer(permissions, many=True)
    return serializer.data
