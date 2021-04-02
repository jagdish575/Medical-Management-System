from django.db import models


class Dealer(models.Model):
    fname = models.CharField(max_length=100)
    lname = models.CharField(max_length=100)
    address = models.TextField()
    phone_number = models.CharField(max_length=15)
    email = models.CharField(max_length=20)


class Medicine(models.Model):
    med_code = models.IntegerField()
    med_name = models.CharField(max_length=50)
    dealer_name = models.ForeignKey(Dealer, on_delete=models.CASCADE)
    price = models.IntegerField()
    stock = models.IntegerField()
    description = models.TextField()


class Employee(models.Model):
    emp_id = models.IntegerField()
    fname = models.CharField(max_length=100)
    lname = models.CharField(max_length=100)
    address = models.TextField()
    salary = models.IntegerField()
    phone_number = models.CharField(max_length=15)
    email = models.CharField(max_length=20)


class Customer(models.Model):
    fname = models.CharField(max_length=100)
    lname = models.CharField(max_length=100)
    address = models.TextField()
    phone_number = models.CharField(max_length=15)
    email = models.CharField(max_length=20)


class Purchase(models.Model):
    prod_name = models.CharField(max_length=100)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    price_number = models.IntegerField()
    quantity = models.IntegerField()