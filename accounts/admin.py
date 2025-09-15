from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from accounts import forms, models


@admin.register(models.CustomUser)
class UserMainAdmin(UserAdmin):
    add_form = forms.CustomUserCreateForm
    form = forms.CustomUserChangeForm
    model = models.CustomUser
    list_display = ('id', 'first_name', 'last_name', 'username', 'email', 'is_staff')
    fieldsets = [
        (None, {'fields': ('username', 'password')}),
        ('Informações Pessoais', {'fields': ('first_name', 'last_name', 'email')}),
        ('Permissões', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Datas Importantes', {'fields': ('last_login', 'date_joined')}),
    ]
    add_fieldsets = (
    (None, {
        'classes': ('wide',),
        'fields': ('email', 'first_name', 'last_name', 'password1', 'password2'),
    }),
    )