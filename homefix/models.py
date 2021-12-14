from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE
from django.db.models.fields.related import OneToOneField

# Create your models here.
class User_type(models.Model):
    user = OneToOneField(User, on_delete=models.CASCADE)
    USER_TYPE_CHOICES = (
      (1, 'customer'),
      (2, 'manager'),
    )
    user_type = models.PositiveSmallIntegerField(choices=USER_TYPE_CHOICES, default=1)

# Create your models here.

class Service_provider(models.Model):
    service_id = models.CharField(max_length=3,primary_key=True)
    service=models.CharField(max_length=20)
    area=models.CharField(max_length=20)
    name=models.CharField(max_length=30)
    contact=models.CharField(max_length=10)
    speciality=models.CharField(max_length=70)
    min_charges=models.IntegerField()
    rating=models.DecimalField(decimal_places=2,max_digits=3)
    max_no_services=models.IntegerField()
    assigned_no_services=models.IntegerField()

class Service_requested(models.Model):
    customer_id = models.ForeignKey(User , on_delete=models.CASCADE)
    customer_name = models.CharField(max_length=30)
    customer_contact_no = models.CharField(max_length=10)
    address = models.CharField(max_length=100)
    requirement = models.CharField(max_length=150)
    service_id = models.ForeignKey(Service_provider,on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    rated = models.IntegerField(null=True)
    status = models.CharField(max_length=10)

class Contact_Us(models.Model):
    name = models.CharField(max_length=30)
    contact_no = models.CharField(max_length=10)
    email = models.EmailField(max_length=30)
    date = models.DateField(auto_now_add=True)
    desc = models.CharField(max_length=100)
    status = models.CharField(max_length=10) 

class Reviews(models.Model):
    service_id = models.ForeignKey(Service_provider, on_delete=models.CASCADE)
    customer_id = models.ForeignKey(User, on_delete=models.CASCADE)
    review = models.CharField(max_length=200)
    rating = models.IntegerField()

