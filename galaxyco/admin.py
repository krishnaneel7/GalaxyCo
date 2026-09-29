from django.contrib import admin

from .models import CustomerRequest


@admin.register(CustomerRequest)
class CustomerRequestAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "name",
        "email",
        "phone",
        "product",
        "quantity",
        "status",
        "created_at",
    )

    list_filter = (
        "status",
        "product",
        "created_at",
    )

    search_fields = (
        "name",
        "email",
        "phone",
        "product",
        "message",
    )

    ordering = (
        "-created_at",
    )

    readonly_fields = (
        "created_at",
    )