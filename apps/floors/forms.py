from django import forms
from apps.floors.models import FloorsVO
from apps.avenues.models import AvenuesVO

class FloorsForm(forms.ModelForm):
    class Meta:
        model = FloorsVO
        fields = ["floors_name", "floors_plan", "floors_slot_price", "floors_avenues_id"]

    # If you want a dropdown instead of a raw ID field
    floors_avenues_id = forms.ModelChoiceField(
        queryset=AvenuesVO.objects.all(), 
        empty_label="Select Avenue", 
        label="Avenue"
    )
