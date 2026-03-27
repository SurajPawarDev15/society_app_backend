from django.contrib import admin

# Register your models here.
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.html import format_html
from .models import User


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    model = User

    # ✅ Fields shown in list view
    list_display = (
        'id',
        'username',
        'email',
        'role',
        'phone',
        'is_staff',
        'is_active',
        'colored_role'
    )

    # ✅ Filters
    list_filter = (
        'role',
        'is_staff',
        'is_active'
    )

    # ✅ Search
    search_fields = (
        'username',
        'email',
        'phone'
    )

    ordering = ('-id',)

    # ✅ Add custom fields to user form
    fieldsets = UserAdmin.fieldsets + (
        ('Additional Info', {
            'fields': ('role', 'phone'),
        }),
    )

    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Additional Info', {
            'fields': ('role', 'phone'),
        }),
    )

    # ✅ Colored Role
    def colored_role(self, obj):
        color = {
            'admin': 'red',
            'resident': 'green',
            'security': 'blue'
        }
        return format_html(
            '<b style="color:{};">{}</b>',
            color.get(obj.role, 'black'),
            obj.role
        )

    colored_role.short_description = "Role"