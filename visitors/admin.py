from django.contrib import admin

# Register your models here.
from django.contrib import admin
from django.utils.html import format_html
from .models import Visitor


@admin.register(Visitor)
class VisitorAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'resident',
        'phone',
        'purpose',
        'status',
        'entry_time',
        'exit_time',
        'created_at',
        'colored_status'
    )

    list_filter = (
        'status',
        'created_at',
        'entry_time',
        'exit_time'
    )

    search_fields = (
        'name',
        'phone',
        'purpose',
        'resident__username'
    )

    ordering = ('-created_at',)

    date_hierarchy = 'created_at'

    readonly_fields = ('created_at',)

    list_per_page = 10

    # ✅ Colored Status
    def colored_status(self, obj):
        color = {
            'pending': 'orange',
            'approved': 'blue',
            'rejected': 'red',
            'entered': 'green',
            'exited': 'gray'
        }
        return format_html(
            '<b style="color:{};">{}</b>',
            color.get(obj.status, 'black'),
            obj.status
        )

    colored_status.short_description = "Status"