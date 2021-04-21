from django.urls import path
from .views import home, register, login, dashboard, \
    dealers, medicines, employees, customers, purchases, confirm_logout

app_name = 'store'

urlpatterns = [
    path('', home, name="home"),
    path('register/', register, name="register"),
    path('login/', login, name="login"),
    path('confirm-logout/', confirm_logout, name="confirm-logout"),
    path('dashboard/', dashboard, name="dashboard"),
    path('dealers/', dealers, name="dealers"),
    path('medicines/', medicines, name="medicines"),
    path('employees/', employees, name="employees"),
    path('customers/', customers, name="customers"),
    path('purchases/', purchases, name="purchases"),
]