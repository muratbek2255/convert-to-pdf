from django.contrib import admin

from src.customer.models import Customer


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    pass
