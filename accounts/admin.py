from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import CustomUser
from .forms import CustomUserChangeForm, CustomUserCreationForm
# Register your models here.

class CustomUserAdmin(UserAdmin):
    ordering = ("email",)
    form = CustomUserChangeForm
    add_form = CustomUserCreationForm
    list_display = ( "email", "first_name", "last_name", "is_staff")

    fieldsets= (
        ("Personal Info", {
            "fields": ('email', 'password', 'first_name', 'last_name')
        }),

        ('Permissions', {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')
        }),

        ('Important Dates', {
            'fields': ('date_joined', 'last_login')
        })
    )
    readonly_fields= ['date_joined', 'last_login']

admin.site.register(CustomUser, CustomUserAdmin)