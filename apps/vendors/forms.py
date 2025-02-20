from django import forms
from .models import VendorVO
class VendorsForm(forms.ModelForm):

    class Meta:
        model = VendorVO
        fields = ['vendors_username', 'vendors_email', 'vendors_password','vendors_phone','vendors_address','vendors_logo']
