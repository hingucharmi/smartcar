import uuid
from django.db import models

class SubscriptionsPlanVO(models.Model):
    id = models.UUIDField(primary_key=False,default=uuid.uuid4,editable=False)
    subscriptions_plan_id = models.AutoField(primary_key=True,null=False)
    subscriptions_plan_name = models.CharField(max_length=200,null=False)
    description = models.CharField(max_length=255,null=False)
    price = models.DecimalField(max_digits=20, decimal_places=2,null=False)
    validity = models.SmallIntegerField(null=False)
    status = models.CharField(max_length=20, choices=[("Paid", "Paid"), ("Due", "Due"), ("Canceled", "Canceled")])
    due_date = models.DateField(null=False)

    def __str__(self):
        return '{} {}'.format(self.subscriptions_plan_name,self.description)

