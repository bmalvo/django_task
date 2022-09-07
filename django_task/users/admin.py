from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from users.models import CustomUser


class CustomUserAdmin(UserAdmin):
    list_display = ('id', 'password','last_login','is_superuser','username','first_name', 
                    'last_name', 'email', 'is_staff', 'is_active', 'date_joined','birthday', 
                    'random_number')


admin.site.register(CustomUser, CustomUserAdmin)
