from django.contrib import admin

# Register your models here.
from django.contrib import admin
from django.utils.html import format_html
from .models import Complaint


@admin.register(Complaint)
class ComplaintAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'title',
        'user',
        'category',
        'priority',
        'status',
        'created_at',
        'colored_status',
        'colored_priority'
    )

    list_filter = (
        'status',
        'category',
        'priority',
        'created_at'
    )

    search_fields = (
        'title',
        'description',
        'user__username'
    )

    ordering = ('-created_at',)

    date_hierarchy = 'created_at'

    readonly_fields = ('created_at',)

    list_per_page = 10

    # ✅ Colored Status
    def colored_status(self, obj):
        color = {
            'pending': 'orange',
            'in_progress': 'blue',
            'resolved': 'green'
        }
        return format_html(
            '<b style="color:{};">{}</b>',
            color.get(obj.status, 'black'),
            obj.status
        )

    colored_status.short_description = "Status"

    # ✅ Colored Priority
    def colored_priority(self, obj):
        color = {
            'low': 'green',
            'medium': 'orange',
            'high': 'red'
        }
        return format_html(
            '<b style="color:{};">{}</b>',
            color.get(obj.priority, 'black'),
            obj.priority
        )

    colored_priority.short_description = "Priority"