from django.contrib import admin
from .models import Order, CustomerProfile


class OrderAdmin(admin.ModelAdmin):
    list_display = [
        "id", "customer", "med_name", "price",
        "timestamp", "quantity"
    ]
    list_display_links = [
        "id", "customer", "med_name"
    ]


class CustomerProfileAdmin(admin.ModelAdmin):
    list_display = [
        "id", "user", 
        "profile_picture", "phone_number"
    ]
    list_display_links = [
        "id", "user"
    ]

admin.site.register(Order, OrderAdmin)
admin.site.register(CustomerProfile)