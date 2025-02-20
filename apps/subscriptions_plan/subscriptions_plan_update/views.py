from django.shortcuts import redirect
from django.contrib import messages
from django.db.models import Q
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from web_project import TemplateLayout
from apps.subscriptions_plan.forms import SubscriptionPlanForm
from apps.subscriptions_plan.models import SubscriptionsPlanVO
from django.contrib.auth.mixins import PermissionRequiredMixin


class SubscriptionPlanUpdateView(TemplateView):
    permission_required = ("subscriptions_plan.change_subscriptions_plan")


    def get_context_data(self, **kwargs):
        context = TemplateLayout.init(self, super().get_context_data(**kwargs))
        context['subscriptions_plan'] = self.get_subscriptionsplan(self.kwargs['pk'])
        return context

    def post(self, request, pk):
        subscriptionsplan = self.get_subscriptionsplan(pk)
        form = SubscriptionPlanForm(request.POST, instance=subscriptionsplan)
        if form.is_valid():
            if not self.subscriptionsplan_exists(form.cleaned_data, subscriptionsplan):
                form.save()
                messages.success(request, 'Subscriptionsplan Updated')
            else:
                messages.error(request, 'Subscriptionsplan Already Exists')
        else:
            messages.error(request, 'Subscriptionsplan Failed')
        return redirect('subscriptionsplan')

    def get_subscriptionsplan(self, pk):
        return SubscriptionsPlanVO.objects.get(pk=pk)

    def subscriptionsplan_exists(self, cleaned_data, current_subscriptionsplan):
        matching_subscriptionsplan = SubscriptionsPlanVO.objects.filter(
            Q(subscriptions_plan_name=cleaned_data['subscriptions_plan_name']) &
            Q(description=cleaned_data['description']) &
            Q(price=cleaned_data['price']) &
            Q(validity=cleaned_data['validity']) &
            Q(status=cleaned_data['status'])&
            Q(due_date=cleaned_data['due_date'])
        ).exclude(pk=current_subscriptionsplan.pk)
        return matching_subscriptionsplan.exists()
