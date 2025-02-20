from django import forms
from .models import SlotsVO


class SlotsForm(forms.ModelForm):

    class Meta:
        model = SlotsVO
        fields = '__all__'

