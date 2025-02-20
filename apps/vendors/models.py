import uuid
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from apps.avenues.models import AvenuesVO


class VendorVO(models.Model):
    vendors_id = models.AutoField(primary_key=True,null=False)
    vendors_username = models.CharField(max_length=100,null=False)
    vendors_email = models.EmailField(max_length=100,null=False)
    vendors_password = models.CharField(max_length=100,null=False)
    vendors_phone = models.CharField(blank=False, max_length=30,null=False)
    vendors_address = models.TextField(max_length=100,null=False)
    vendors_logo = models.ImageField(null=True,blank=True , upload_to="vendors/")
    vendors_avenues = models.ForeignKey("avenues.AvenuesVO", on_delete=models.CASCADE,default=1)

        
    id = models.UUIDField(primary_key=False,default=uuid.uuid4,editable=False)

    def __str__(self):
        return self.vendors_username
    
    class Meta:
        db_table = "vendors"
        unique_together = ['vendors_email','vendors_phone','vendors_username']


