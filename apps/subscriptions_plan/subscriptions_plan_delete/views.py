from django.shortcuts import redirect, get_object_or_404
from django.views.generic import DeleteView
from django.contrib import messages
from apps.subscriptions_plan.models import SubscriptionsPlanVO
from django.contrib.auth.mixins import PermissionRequiredMixin

class SubscriptionsPlanDeleteView(DeleteView):

    permission_required = ("subscriptions_plan.delete_subscriptions_plan")


    def get(self, request, pk):
        subscriptionsplan = get_object_or_404(SubscriptionsPlanVO, subscriptions_plan_id=pk)
        subscriptionsplan.delete()
        messages.success(request, 'Subscriptions Deleted')
        return redirect('subscriptionsplan')
