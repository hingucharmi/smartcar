from time import localtime
import uuid
from django.db import models
from apps.customers.models import Customers
from apps.slots.models import SlotsVO


class BookingVO(models.Model):
    bookings_id = models.AutoField(primary_key=True,null=False)
    bookings_customers = models.ForeignKey("customers.Customers",on_delete=models.CASCADE)
    bookings_slots = models.ForeignKey("slots.SlotsVO",on_delete=models.CASCADE)
    bookings_price = models.DecimalField(max_digits=20, decimal_places=2,null=False)
    start_date = models.DateField() 
    end_date = models.DateField()   
    created_ts = models.DateTimeField(auto_now_add=True)  
    updated_ts = models.DateTimeField(auto_now=True)   
    deleted_ts = models.DateTimeField(null=True, blank=True) 

    id = models.UUIDField(primary_key=False,default=uuid.uuid4,editable=False)

    def __str__(self):
        return f"Booking {self.bookings_id} | Customer: {self.bookings_customers} | Slot: {self.bookings_slots} | Price: {self.bookings_price} "
    
    class Meta:
        db_table = "booking"


