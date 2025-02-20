from datetime import date
from django.db import models
from apps.customers.models import Customers
from apps.subscriptions_plan.models import SubscriptionsPlanVO

 

# Create your models here.
class SubscriptionsVO(models.Model):
    subscriptions_id = models.AutoField(primary_key=True)

    subscriptions_price = models.DecimalField(decimal_places=2,max_digits=20, null=False)
    
    subscriptions_validity = models.DecimalField(decimal_places=2,max_digits=20, null=False)

    subscriptions_customers = models.ForeignKey('customers.Customers', on_delete=models.CASCADE) 
    #  here we use customers= app name and model name
    
    subscriptions_subscriptionsplans = models.ForeignKey('subscriptions_plan.SubscriptionsPlanVO',on_delete=models.CASCADE)
    
    start_ts = models.DateField() 
    
    end_ts = models.DateTimeField(auto_now=True)
    

    # def start_ts(self):
    #      event = date.self.start_ts
    #      day_till = self.subscriptions_validity.date() + self.start_ts 
         
    #      return day_till

    def __str__(self):
        return f"{self.subscriptions_customers} - {self.subscriptions_subscriptionsplans}"

    class Meta:
        db_table = "subscriptions"
