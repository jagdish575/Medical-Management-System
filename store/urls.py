from django import path
from .views import home, register, login, dashboard, \
    dealers, medicines, employees, customers, purchases

urlpatterns = [
    path('', home, name="home"),
    path('register/', register, name="register"),
    path('login/', login, name="login"),
    path('dashboard/', dashboard, name="dashboard"),
    path('dealers/', dealers, name="dealers"),
    path('medicines/', medicines, name="medicines"),
    path('employees/', employees, name="employees"),
    path('customers/', customers, name="customers"),
    path('purchases/', purchases, name="purchases"),
]