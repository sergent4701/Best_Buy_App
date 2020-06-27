from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User
from django.contrib.auth import get_user_model

User = get_user_model()


class UserAdmin(admin.ModelAdmin):
    search_fields = ['username']

    class Meta:
        model = User


admin.site.register(User, UserAdmin)

# class UserAdmin(BaseUserAdmin):
#     list_display = ('username', 'full_name', 'employee_type', 'is_active', 'is_staff', 'is_admin', 'is_superuser', 'date_joined', 'last_login')
#

# admin.site.register(User, UserAdmin)