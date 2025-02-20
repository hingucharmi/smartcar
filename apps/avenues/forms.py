from django import forms
from .models import AvenuesVO

class AvenuesForm(forms.ModelForm):
    class Meta:
        model = AvenuesVO
        fields = '__all__'
        