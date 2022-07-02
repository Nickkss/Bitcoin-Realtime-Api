from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.html import format_html

from .models import User
# Register your models here.


class CustomUserAdmin(UserAdmin):
    model = User

    list_display = ('email', 'name', 'is_active', 'last_login')
    list_filter = ('is_staff', 'is_active',)
    fieldsets = (
        ("Credentials", {'fields': ('email', 'password')}),
        ('Personal Info', {'fields': ('name', )}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Contact Info', {'fields':('phone',)}),
        ('Important Dates', {'fields':('date_joined', 'last_login',)})
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'is_staff', 'is_active')}
        ),
    )
    search_fields = ('email',)
    ordering = ('email',)

admin.site.register(User, CustomUserAdmin)