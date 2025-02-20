from django.views.generic import TemplateView , ListView , UpdateView,DeleteView
from web_project import TemplateLayout
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render , redirect
from apps.subscriptions.models import *
from apps.subscriptions_plan.models import *
from apps.customers.models import *
from django.views import View
from django.urls import reverse_lazy
from django.contrib import messages

"""
This file is a view controller for multiple pages as a module.
Here you can override the page view layout.
Refer to academy/urls.py file for more pages.
"""
 # Predefined function

  
class SubscriptionsAddView(TemplateView):
    permission_required = ("subscriptions.add_subscriptions")

    def get_context_data(self, **kwargs):
        # A function to init the global layout. It is defined in web_project/__init__.py file
        context = TemplateLayout.init(self, super().get_context_data(**kwargs))
        return context

    def get(self, request):
        return render(request, "subscriptionlist.html")  # Render form for new avenue

    def post(self, request):
        customers = Customers.objects.get(customers_id=request.POST.get("customers_id"))
        subscriptionsplan = SubscriptionsPlanVO.objects.get(subscriptions_plan_id=request.POST.get("subscriptions_plan_id"))
        print(customers," post customers")
        print(subscriptionsplan,"post subscriptionsplan")

        subscriptions = SubscriptionsVO(
            subscriptions_price = request.POST.get("subscriptions_price"),
            subscriptions_validity = request.POST.get("subscriptions_validity"),
            start_ts = request.POST.get("start_ts"),
            end_ts = request.POST.get("end_ts"),

            subscriptions_customers = customers,
            subscriptions_subscriptionsplans = subscriptionsplan,

        )
        subscriptions.save()
        messages.success(request,'Subscriptions Added Successfully..!')
        print(subscriptions,"post subscriptions")

        return redirect("subscriptions")  # Redirect to list view after saving
    

    

class SubscriptionsListView(ListView):
    model = SubscriptionsVO
    template_name = 'subscriptionlist.html'  # Template path

    def get_context_data(self, **kwargs):
        customers_dict = Customers.objects.all()
        subscriptionsplan_dict = SubscriptionsPlanVO.objects.all()

        # A function to init the global layout. It is defined in web_project/__init__.py file
        context = TemplateLayout.init(self, super().get_context_data(**kwargs))

        try:
            subscriptions_dict = SubscriptionsVO.objects.all().order_by("subscriptions_id")
            customers_dict = Customers.objects.all()
            subscriptionsplan_dict = SubscriptionsPlanVO.objects.all()
            # print(customers_dict )
            # print(subscriptions_dict)
            # print(subscriptionsplan_dict  )
            context['subscriptions_dict'] = subscriptions_dict  # Add to context
            context['customers_dict'] = customers_dict  # Add to context
            context['subscriptionsplan_dict'] = subscriptionsplan_dict  # Add to context
        except Exception as e:
            print(f'{e} - Error while fetching subscriptions')
            context['subscriptions_dict'] = None,
            context['customers_dict'] = None ,
            context['subscriptionsplan_dict'] = None
        return context
    
    def get_queryset(self):             
        return SubscriptionsVO.objects.all().order_by('subscriptions_id')

class SubscriptionsUpdateView(UpdateView):
    permission_required = ("subscriptions.change_subscriptions")

    model = SubscriptionsVO
    fields = [
        "subscriptions_price","subscriptions_validity","start_ts","subscriptions_customers"
    ]
    template_name = "subscriptions_update.html"
    def get_success_url(self):
        messages.success(self.request,'Subscriptions Updated Successfully.!')
        return reverse_lazy("subscriptions")

    def get_context_data(self, **kwargs):
        # A function to init the global layout. It is defined in web_project/__init__.py file
        context = TemplateLayout.init(self, super().get_context_data(**kwargs))
        context['subscriptions'] = self.get_subscriptions(self.kwargs['pk'])
        context['customers_dict'] = Customers.objects.all()
        context['subscriptionsplan_dict'] = SubscriptionsPlanVO.objects.all()

        return context
    def get_subscriptions(self, pk):
        return SubscriptionsVO.objects.get(pk=pk)
    
class SubscriptionsDeleteView(DeleteView):
    permission_required = ("subscriptions.delete_subscriptions")

    model = SubscriptionsVO

    def get(self, request, pk):
        devices = get_object_or_404(SubscriptionsVO, subscriptions_id=pk)
        devices.delete()
        messages.success(request, 'Successfully Deleted')
        return redirect('subscriptions')

        
 