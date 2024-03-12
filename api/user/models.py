from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager

# gettext_lazy is a function used for translating text in Django applications.
# It is similar to the gettext
from django.utils.translation import gettext_lazy as _


class CustomUserManager(UserManager):

    def create_user(self, email, password=None, role=None, **extra_fields):
        if not email:
            raise ValueError('Email is required')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.set_role(role)
        user.save(using=self.db)
        return user

    def create_superuser(self, email, password=None, role=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(email, password, role, **extra_fields)


class User(AbstractUser):
    objects = CustomUserManager()

    email = models.CharField(_('email address'), unique=True)
    username = models.CharField(_('username'), max_length=150, null=True, blank=True)
    avatar = models.FileField(upload_to='user_avatars')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def set_role(self, role):
        if self.role:
            user_role = UserRole.objects.get(name=role)
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
