from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager

# gettext_lazy is a function used for translating text in Django applications.
# It is similar to the gettext
from django.utils.translation import gettext_lazy as _


class CustomUserManager(UserManager):

    def create_user(self, email, username, password=None, **extra_fields):
        if not email:
            raise ValueError('Email is required')
        if not username:
            raise ValueError('Username is required')
        email = self.normalize_email(email)
        username = self.normalize_email(username)
        user = self.model(email=email, username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(email, username, password, **extra_fields)


class User(AbstractUser):
    email = models.CharField(_('email address'), unique=True)
    username = models.CharField(_('username'), max_length=50, unique=True, blank=False, null=False)

    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    def set_role(self, role):
        if self.role:
            user_role = UserRole.objects.get(role=role)
            user_role.user_role = role
            user_role.save()
        else:
            UserRole.objects.create(user_role=role, user=self)

    @property
    def role(self):
        user_role = UserRole.objects.filter(user=self)
        return user_role.first().user_role if user_role else ""


class Role(models.Model):
    SUPER_ADMIN = 'SUPER_ADMIN'
    ADMIN = 'ADMIN'
    USER = 'USER'

    ROLE_NAME_CHOICES = [
        (SUPER_ADMIN, "Dark lord"),
        (ADMIN, "Admin"),
        (USER, "User")
    ]

    name = models.CharField(max_length=50, choices=ROLE_NAME_CHOICES, default='User', unique=True)

    def __str__(self):
        return self.name


class UserRole(models.Model):
    user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True, related_name='user_role')
    user_role = models.ForeignKey(Role, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.user.username} - {self.user_role.name}"
