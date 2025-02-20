from django import forms
from .models import SubscriptionsPlanVO

class SubscriptionPlanForm(forms.ModelForm):
    class Meta:
        model = SubscriptionsPlanVO
        fields = ['subscriptions_plan_name', 'description', 'price','validity','status','due_date']
