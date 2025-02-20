from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.views.generic import TemplateView , ListView , DeleteView ,UpdateView
from django.db.models import Sum
from web_project.template_helpers.theme import TemplateHelper
from web_project import TemplateLayout
from django.views import View
from apps.subscriptions.models import SubscriptionsVO
from apps.subscriptions_plan.models import SubscriptionsPlanVO
from apps.customers.models import Customers
from apps.subscriptions.forms import SubscriptionsForm


class SubscriptionsListView(ListView):
    
    model = SubscriptionsVO , SubscriptionsPlanVO , Customers
    template_name = 'subscriptionlist.html'  # Template path

    def get_context_data(self, **kwargs):
        subscriptions = SubscriptionsVO.objects.all()
        # A function to init the global layout. It is defined in web_project/__init__.py file
        context = TemplateLayout.init(self, super().get_context_data(**kwargs)) 
        try:
            subscriptions_dict = SubscriptionsVO.objects.all().order_by('subscriptions_id')
            
            subscriptionsplan_dict = SubscriptionsPlanVO.objects.all()
            customers_dict = Customers.objects.all()

            print( customers_dict ," customers")
            print( subscriptionsplan_dict ," subscriptionsplan")

            context['subscriptions'] = subscriptions_dict  # Add to context
            context['subscriptionsplan'] = subscriptionsplan_dict
            context['customers'] = customers_dict

        except Exception as e:
            print(f'{e} - Error while fetching AvenuesVO')
            context['subscriptions_dict'] = None  # Handle errors gracefully

            

        return context
    def get_queryset(self):         
        return SubscriptionsVO.objects.all().order_by('subscriptions_id')



class SubscriptionsAddView(TemplateView):
    def get_context_data(self, **kwargs):
        # A function to init the global layout. It is defined in web_project/__init__.py file
        context = TemplateLayout.init(self, super().get_context_data(**kwargs))

        return context
    def get(self, request):
        return render(request, "subscriptionlist.html")  # Render form for new avenue

    def post(self, request):
        customers = Customers.objects.get(customers_id=request.POST.get("customers_id"))
        subscriptionsplan = SubscriptionsPlanVO.objects.get(subscriptions_plan_id=request.POST.get("subscriptions_plan_id"))

        subscriptions = SubscriptionsVO(
            subscriptions_price = request.POST.get("subscriptions_price"),
            subscriptions_validity = request.POST.get("subscriptions_validity"),
            start_ts = request.POST.get("start_ts"),
            end_ts = request.POST.get("end_ts"),

            subscriptions_customers = customers,
            subscriptions_subscriptionsplans = subscriptionsplan

        )
        subscriptions.save()
        return redirect("subscriptions")  # Redirect to list view after saving
    