from django.db import models
from django.contrib.auth.hashers import make_password, check_password
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
class Customers(models.Model):
    customers_id = models.AutoField(primary_key=True,null=False)
    customers_firstname = models.CharField(max_length=40, default='',null=False)
    customers_middlename = models.CharField(max_length=40, default='',null=False)
    customers_lastname = models.CharField(max_length=40, default='',null=False)
    customers_username = models.CharField(max_length=40, default='',null=False)
    customers_email = models.EmailField(max_length=25,null=False)
    customers_password = models.CharField(max_length=40, default='',null=False)
    customers_phone = models.CharField(max_length=40, null=False,blank=False, unique=True)
    customers_avatar = models.ImageField(upload_to='customers/',null=True,blank=True)
    
    
    def _str__(self):
        return '{} {} {}'.format(self.customers_firstname,self.customers_middlename,self.customers_lastname,self.customers_username)
    
    class Meta:
        db_table = "customers"
        unique_together = ['customers_email','customers_phone','customers_username']

