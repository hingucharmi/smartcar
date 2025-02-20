from django import forms
from .models import DevicesVO

class DevicesForm(forms.ModelForm):
    class Meta:
        model = DevicesVO
        fields = '__all__'
