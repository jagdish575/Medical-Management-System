from django.urls import path
from .views import home_page, register_page, login_page, dashboard_page, \
    dealers_page, medicines_page, employees_page, customers_page, purchases_page,\
        confirm_logout_page

app_name = 'store'

urlpatterns = [
    path('', home_page, name="home"),
    path('register/', register_page, name="register"),
    path('login/', login_page, name="login"),
    path('confirm-logout/', confirm_logout_page, name="confirm-logout"),
    path('dashboard/', dashboard_page, name="dashboard"),
    path('dealers/', dealers_page, name="dealers"),
    path('medicines/', medicines_page, name="medicines"),
    path('employees/', employees_page, name="employees"),
    path('customers/', customers_page, name="customers"),
    path('purchases/', purchases_page, name="purchases"),
]