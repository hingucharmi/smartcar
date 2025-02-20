from django.db import models


# Create your models here.
class AvenuesVO(models.Model):
    avenues_id = models.AutoField(db_column="avenues_id", primary_key=True,
                                   null=False)
    
    avenues_name = models.CharField(db_column="avenues_name",max_length=25, default='',null=False,unique=True)
    avenues_username = models.CharField(db_column="avenues_username",max_length=255, default='',null=False,unique=True)
    avenues_email = models.CharField(db_column="avenues_email",max_length=30, default='',null=False,unique=True)
    avenues_password = models.CharField(db_column="avenues_password",max_length=18, default='',null=False,unique=True)
    avenues_address = models.TextField(db_column="avenues_address",max_length=255, default='',null=False)
    avenues_slot_price = models.CharField(db_column="avenues_slot_price",max_length=20, default='',null=False,)
    avenues_logo = models.ImageField(null=True,blank=True,upload_to='avenues/')
    avenues_country = models.CharField(db_column="avenues_country",max_length=30, default='',null=False)
    avenues_state = models.CharField(db_column="avenues_state",max_length=30, default='',null=False)
    avenues_city = models.CharField(db_column="avenues_city",max_length=30, default='',null=False)
    avenues_pincode = models.CharField(db_column="avenues_pincode",max_length=10, default='',null=False)

    def __str__(self):
        return '{} {}'.format(self.avenues_name, self.avenues_username)

    class Meta:
        db_table = "avenues_table"
        unique_together = ['avenues_username','avenues_email','avenues_password']
       
