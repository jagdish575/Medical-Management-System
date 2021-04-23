from django.urls import path
from .views import home_page, register_page, login_page, dashboard_page, \
    dealers_page, medicines_page, employees_page, customers_page, purchases_page,\
        confirm_logout_page, add_dealer_page, add_medicine_page, add_employee_page,\
            logout, add_customer_page, add_purchase_page, settings_page, update_dealer,\
                delete_dealer

app_name = 'store'

urlpatterns = [
    path('', home_page, name="home"),
    path('register/', register_page, name="register"),
    path('login/', login_page, name="login"),
    path('confirm-logout/', confirm_logout_page, name="confirm-logout"),
    path('confirm-logout/logout/', logout, name="logout"),
    path('dashboard/', dashboard_page, name="dashboard"),

    # Dealer CRUD
    path('dealers/', dealers_page, name="view-dealers"),
    path('dealers/add-dealer/', add_dealer_page, name="add-dealer"),
    path('dealers/update-dealer/<int:pk>/', update_dealer, name="update-dealer"),
    path('dealers/delete-dealer/<int:pk>/', delete_dealer, name="delete-dealer"),


    path('medicines/', medicines_page, name="view-medicines"),
    path('medicines/add-medicine/', add_medicine_page, name="add-medicine"),
    path('employees/', employees_page, name="view-employees"),
    path('employees/add-employee/', add_employee_page, name="add-employee"),
    path('customers/', customers_page, name="view-customers"),
    path('customers/add-customer/', add_customer_page, name="add-customer"),
    path('purchases/', purchases_page, name="view-purchases"),
    path('purchases/add-purchase/', add_purchase_page, name="add-purchase"),
    path('settings/', settings_page, name="settings")
]