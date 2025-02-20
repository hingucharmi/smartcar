import uuid
from django.db import models

class ZonesVO(models.Model):
    zones_id = models.AutoField(primary_key=True,null=False)
    zones_floors_id = models.ForeignKey('floors.FloorsVO', on_delete=models.CASCADE)
    zones_name = models.CharField(max_length=200,null=False)
    zones_capacity = models.SmallIntegerField(null=False)
    zones_slot_price = models.DecimalField(max_digits=20, decimal_places=2,null=False)
    id = models.UUIDField(primary_key=False,default=uuid.uuid4,editable=False)

    def __str__(self):
        return '{} {} {} {} {}'.format(self.zones_name , self.zones_capacity, self.zones_floors_id , self.zones_capacity ,self.zones_slot_price)

