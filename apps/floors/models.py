from django.db import models


# Create your models here.
class FloorsVO(models.Model):
    floors_id = models.AutoField(db_column="floors_id",primary_key=True,null=None)

    
    floors_name = models.CharField(db_column="floors_name",max_length=25, default='',null=False)
    
    floors_plan = models.CharField(db_column="floors_plan",default='', null=False)
    
    floors_slot_price = models.DecimalField(db_column="floors_slot_price",decimal_places=2,max_digits=20, null=False)
    
    floors_avenues_id = models.ForeignKey('avenues.AvenuesVO',db_column="floors_avenues_id", on_delete=models.CASCADE)
    
    def __str__(self):
        return '{} {}'.format(self.floors_name, self.floors_plan) 

    class Meta:
        db_table = "floor_table"
        unique_together = ['floors_name','floors_plan']
