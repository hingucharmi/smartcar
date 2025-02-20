import uuid
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from apps.avenues.models import AvenuesVO
from apps.vendors.models import VendorVO


class DevicesVO(models.Model):
    devices_id = models.AutoField(primary_key=True,null=False)
    devices_name = models.CharField(max_length=100,null=False)
    devices_mac = models.CharField(max_length=100,null=False)
    devices_type = models.BigIntegerField(null=False)
    devices_image = models.CharField(max_length=100,null=False)
    devices_state = models.CharField(max_length=100,null=False)
    devices_status = models.SmallIntegerField()
    devices_avenues = models.ForeignKey("avenues.AvenuesVO", on_delete=models.CASCADE)
    devices_vendors = models.ForeignKey("vendors.VendorVO", on_delete=models.CASCADE)

    id = models.UUIDField(primary_key=False,default=uuid.uuid4,editable=False)

    def __str__(self):
        return self.devices_name
    
    class Meta:
        db_table = "devices"


