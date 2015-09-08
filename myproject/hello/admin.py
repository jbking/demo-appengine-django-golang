from django import forms
from django.contrib import admin
from django.contrib.admin.sites import NotRegistered
from django.contrib.auth.admin import UserAdmin
from .models import Greeting, User


admin.site.register(Greeting)


# This is ignore displaying that Custom User may also many-to-many to Group
# https://github.com/django-nonrel/djangotoolbox/issues/46
class UserForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'is_active',
                  'is_staff', 'is_superuser')


class CustomUserAdmin(UserAdmin):
    fieldsets = None
    form = UserForm
    search_fields = ('=username',)
    list_filter = ('is_staff', 'is_superuser', 'is_active')

try:
    admin.site.register(User, CustomUserAdmin)
except NotRegistered:
    pass
