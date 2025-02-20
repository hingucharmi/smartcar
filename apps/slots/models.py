import uuid
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from apps.vendors.models import VendorVO
from apps.zones.models import ZonesVO
from apps.devices.models import DevicesVO


class SlotsVO(models.Model):
    slots_id = models.AutoField(primary_key=True,null=False)
    slots_name = models.CharField(max_length=100,null=False)
    slots_zones = models.ForeignKey("zones.ZonesVO", on_delete=models.CASCADE)
    slots_vendors = models.ForeignKey("vendors.VendorVO",on_delete=models.CASCADE)
    slots_devices = models.OneToOneField("devices.DevicesVO",on_delete=models.CASCADE)
    slots_price = models.DecimalField(max_digits=20, decimal_places=2,null=False)
    slots_status = models.SmallIntegerField(default=0)

    id = models.UUIDField(primary_key=False,default=uuid.uuid4,editable=False)

    def __str__(self):
        return self.slots_name
    
    class Meta:
        db_table = "slots"


