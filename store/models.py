from django.db import models


class Dealer(models.Model):
    fname = models.CharField(max_length=100)
    lname = models.CharField(max_length=100)
    address = models.TextField()
    phone_number = models.CharField(max_length=15)
    email = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.fname} {self.lname}" 


class Medicine(models.Model):
    med_code = models.IntegerField()
    med_name = models.CharField(max_length=50)
    dealer_name = models.ForeignKey(Dealer, on_delete=models.CASCADE)
    price = models.FloatField()
    stock = models.IntegerField()
    description = models.TextField()

    def __str__(self):
        return f"{self.med_code}: {self.med_name}"


class Employee(models.Model):
    emp_id = models.IntegerField()
    fname = models.CharField(max_length=100)
    lname = models.CharField(max_length=100)
    address = models.TextField()
    salary = models.FloatField()
    phone_number = models.CharField(max_length=15)
    email = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.emp_id}: {self.fname} {self.lname}"


class Customer(models.Model):
    fname = models.CharField(max_length=100)
    lname = models.CharField(max_length=100)
    address = models.TextField()
    phone_number = models.CharField(max_length=15)
    email = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.fname} {self.lname}"


class Purchase(models.Model):
    med_name = models.ForeignKey(Medicine, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    price_number = models.FloatField()
    quantity = models.IntegerField()

    def __str__(self):
        return f"{self.med_name} {self.customer}"



"""
NOTE:
- get_absolute_url method
- get_update_url method
- get_delete_url method
"""