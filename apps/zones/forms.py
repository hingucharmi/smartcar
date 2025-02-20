from django import forms
from .models import ZonesVO

class ZonesVOForm(forms.ModelForm):
    class Meta:
        model = ZonesVO
        fields = ['zones_name', 'zones_capacity', 'zones_slot_price']  