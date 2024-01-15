from django.contrib import admin

from .models import User, Role, UserRole
from .forms import UserForm


class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'email', 'get_role', 'is_active', 'is_staff', 'is_superuser')
    exclude = ('is_staff', 'is_superuser')
    form = UserForm

    def get_form(self, request, obj=None, **kwargs):
        kwargs['form'] = UserForm
        form = super().get_form(request, obj=None, **kwargs)
        available_roles = ["SUPER_ADMIN", "ADMIN", "USER"]
        form.base_fields['role'].choices = available_roles
        if obj and obj.role:
            form.base_fields['role'].initial = [obj.role.name]
        return form

    def get_role(self, user):
        return user.role


admin.site.register(User, UserAdmin)
admin.site.register(Role)
admin.site.register(UserRole)
