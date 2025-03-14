from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ('id','email', 'first_name', 'last_name', 'is_staff', 'is_active')
    list_display_links = ('id', 'email')
    list_filter = ('is_staff', 'is_active')
    readonly_fields = ('last_login', 'date_joined')
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'user_type')}),
        ('Permissions', {'fields': ('is_staff', 'is_active', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'is_staff', 'is_active', 'user_type')}
        ),
    )
    # list_display = UserAdmin.list_display + ('user_type',)
    search_fields = ('email',)
    ordering = ('-date_joined',)

admin.site.register(CustomUser, CustomUserAdmin)
