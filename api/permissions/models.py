from django.db import models

# Create your models here.
from .permissions import PERMISSION_CHOICES
from user.models import Role


class UserRolePermission(models.Model):
    user_role = models.ForeignKey(Role, on_delete=models.SET_NULL, null=True)
    permission = models.CharField(choices=PERMISSION_CHOICES, max_length=120, null=True)
