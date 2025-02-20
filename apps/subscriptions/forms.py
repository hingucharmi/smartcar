from django import forms
from .models import SubscriptionsVO

class SubscriptionsForm(forms.ModelForm):
    class Meta:
        model = SubscriptionsVO
        fields = '__all__'
