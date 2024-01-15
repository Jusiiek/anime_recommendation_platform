from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.urls import reverse_lazy

from .models import Role


def edit_user_password_text():
    return f"To set a password click on the link <a href=\"{reverse_lazy('admin:password_change')}\">here</a>"


class UserForm(forms.ModelForm):
    CHOICES = (
        ("SUPER_ADMIN", "SUPER_ADMIN"),
        ("ADMIN", "ADMIN"),
        ("USER", "USER")
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance.pk:
            self.fields["password"].help_text = edit_user_password_text()

    role = forms.ChoiceField(choices=CHOICES)
    password = ReadOnlyPasswordHashField()

    def save(self, commit=True, **kwargs):
        user = super().save(commit)
        user.set_password(self.cleaned_data.get("password"))
        role = self.cleaned_data.get("role")
        user.is_superuser = role == "SUPER_ADMIN"
        role = Role.objects.get(name=role)
        user.save()
        user.set_role(role)
        user.save()
        return user
