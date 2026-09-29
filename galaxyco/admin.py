from django.contrib import admin

from .models import CustomerRequest


@admin.register(CustomerRequest)
class CustomerRequestAdmin(
    admin.ModelAdmin
):

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

        "created_at",

    )


    search_fields = (

        "name",

        "email",

        "phone",

        "product",

    )


    ordering = (

        "-created_at",

    )