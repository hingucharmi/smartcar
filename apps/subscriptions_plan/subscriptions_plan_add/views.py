from django.shortcuts import redirect, render
from django.views.generic import TemplateView , ListView
from django.db.models import Sum
from web_project.template_helpers.theme import TemplateHelper
from web_project import TemplateLayout
from django.views import View
from apps.subscriptions_plan.models import SubscriptionsPlanVO
from django.contrib import messages

class SubscriptionsPlanAddView(View):
    permission_required = ("subscriptions_plan.add_subscriptions_plan")

    
    def get_context_data(self, **kwargs):
        # A function to init the global layout. It is defined in web_project/__init__.py file
        context = TemplateLayout.init(self, super().get_context_data(**kwargs))

        return context
    def get(self, request):
        return render(request, "subscriptions_plan_list.html")  # Render form for new avenue

    def post(self, request):
       
        subscritpionsplans = SubscriptionsPlanVO(
            subscriptions_plan_name = request.POST.get("subscriptions_plan_name"),
            description = request.POST.get("description"),
            price = request.POST.get("price"),
            validity = request.POST.get("validity"),
            status = request.POST.get("status"),
            due_date = request.POST.get("due_date"),

        )
        subscritpionsplans.save()
        messages.success(request,'Subscription Plans Added Successfully..!')
        return redirect("subscriptionsplan")  # Redirect to list view after saving
    