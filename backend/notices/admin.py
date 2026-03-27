from django.contrib import admin

# Register your models here.
from django.contrib import admin
from django.utils.html import format_html
from .models import Notice


@admin.register(Notice)
class NoticeAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'title',
        'created_by',
        'notice_type',
        'expiry_date',
        'created_at',
        'colored_type'
    )

    list_filter = (
        'notice_type',
        'expiry_date',
        'created_at'
    )

    search_fields = (
        'title',
        'message',
        'created_by__username'
    )

    ordering = ('-created_at',)

    date_hierarchy = 'created_at'

    readonly_fields = ('created_at',)

    list_per_page = 10

    # ✅ Colored Notice Type
    def colored_type(self, obj):
        color = {
            'general': 'blue',
            'important': 'red',
        }
        return format_html(
            '<b style="color:{};">{}</b>',
            color.get(obj.notice_type, 'black'),
            obj.notice_type
        )

    colored_type.short_description = "Type"