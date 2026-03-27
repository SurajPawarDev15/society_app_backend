from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Payment


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'user',
        'amount',
        'month',
        'status',
        'due_date',
        'paid_at',
        'created_at'
    )

    list_filter = (
        'status',
        'month',
        'due_date',
        'created_at'
    )

    search_fields = (
        'user__username',
        'month',
        'status'
    )

    ordering = ('-created_at',)

    date_hierarchy = 'created_at'

    readonly_fields = ('created_at',)

    list_per_page = 10