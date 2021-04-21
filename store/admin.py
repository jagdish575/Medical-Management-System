from django.contrib import admin
from .models import Dealer, Medicine, Employee, \
    Customer, Purchase


class DealerAdmin(admin.ModelAdmin):
    list_display = [
        'id', 'fname', 'lname',
        'address', 'phone_number', 'email'
    ]


class MedicineAdmin(admin.ModelAdmin):
    list_display = [
        'id', 'med_code', 'med_name', 'dealer_name',
        'price', 'stock', 'description'
    ]


class EmployeeAdmin(admin.ModelAdmin):
    list_display = [
        'id', 'emp_id', 'fname', 'lname',
        'address', 'salary', 'phone_number', 'email'
    ]


class CustomerAdmin(admin.ModelAdmin):
    list_display = [
        'id', 'fname', 'lname', 'address',
        'phone_number', 'email'
    ]


class PurchaseAdmin(admin.ModelAdmin):
    list_display = [
        'id', 'med_name', 'customer',
        'price_number', 'quantity'
    ]


admin.site.register(Dealer, DealerAdmin)
admin.site.register(Medicine, MedicineAdmin)
admin.site.register(Employee, EmployeeAdmin)
admin.site.register(Customer, CustomerAdmin)
admin.site.register(Purchase, PurchaseAdmin)