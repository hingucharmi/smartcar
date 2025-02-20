from django.shortcuts import redirect, render
from django.views.generic import TemplateView , ListView
from django.db.models import Sum
from web_project.template_helpers.theme import TemplateHelper
from web_project import TemplateLayout
from django.views import View
from apps.subscriptions_plan.models import SubscriptionsPlanVO


class SubscriptionsPlanListView(ListView):

    model = SubscriptionsPlanVO
    template_name = 'subscriptions_plan_list.html'  # Template path

    def get_context_data(self, **kwargs):
        subscriptionsplan = SubscriptionsPlanVO.objects.all()
        # A function to init the global layout. It is defined in web_project/__init__.py file
        context = TemplateLayout.init(self, super().get_context_data(**kwargs)) 
        try:
            subscriptionsplan_dict = SubscriptionsPlanVO.objects.all().order_by('subscriptions_plan_id')
            context['subscriptionsplan_dict'] = subscriptionsplan_dict  # Add to context
        except Exception as e:
            print(f'{e} - Error while fetching AvenuesVO')
            context['subscriptionsplan_dict'] = None  # Handle errors gracefully

            

        return context
    def get_queryset(self):   
           
        return SubscriptionsPlanVO.objects.all().order_by('subscriptions_plan_id')
