from django.contrib import admin
from .models import NewUser
from django.contrib.auth.admin import UserAdmin


class UserAdminConfig(UserAdmin):

    search_fields = ('user_name', 'email', 'last_name', 'first_name')
    list_filter = ('user_name', 'email', 'last_name', 'first_name', 'is_active', 'is_staff')
    ordering = ('-start_date',)
    list_display = ('user_name', 'email', 'last_name', 'first_name', 'is_active', 'is_staff')

    fieldsets = (
        ('Basic Information', {'fields': ('user_name', 'email', 'first_name','last_name')}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
        ('Personal', {'fields': ('about',)}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('user_name', 'email', 'first_name', 'last_name', 'password1', 'password2', 'is_active','is_staff')
        }),
    )


admin.site.register(NewUser, UserAdminConfig)