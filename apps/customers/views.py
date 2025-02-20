from django.shortcuts import get_object_or_404, render
from apps.customers.models import Customers
from django.views.generic import TemplateView , ListView , UpdateView,DeleteView
from web_project import TemplateLayout
from django.http import HttpResponse
from django.shortcuts import render , redirect
from django.views import View
from django.urls import reverse_lazy
from django.contrib import messages
# from django.forms import 

# Create your views here.

class CustomersListView(ListView):
    model = Customers
    template_name = 'viewcustomers.html'  # Template path

    def get_context_data(self, **kwargs):
        avenues_dict = Customers.objects.all()
        # A function to init the global layout. It is defined in web_project/__init__.py file
        context = TemplateLayout.init(self, super().get_context_data(**kwargs)) 
        try:
            customers_dict = Customers.objects.all().order_by('customers_id')
            context['customers_dict'] = customers_dict  # Add to context
        except Exception as e:
            print(f'{e} - Error while fetching Customers')
            context['customers_dict'] = None  # Handle errors gracefully

        return context
    def get_queryset(self):   
           
        return Customers.objects.all().order_by('customers_id')




class CustomersAddView(View):
    permission_required = ("customers.add_customers")


    def get_context_data(self, **kwargs):
        # A function to init the global layout. It is defined in web_project/__init__.py file
        context = TemplateLayout.init(self, super().get_context_data(**kwargs))

        return context
    def get(self, request):
        return redirect("customers")

    def post(self, request):
       
        customers_obj = Customers(

            customers_firstname = request.POST.get("customers_firstname"),
            customers_middlename =request.POST.get("customers_middlename"),
            customers_lastname = request.POST.get("customers_lastname"),
            customers_username = request.POST.get("customers_username"),
            customers_email =request.POST.get("customers_email"),
            customers_password = request.POST.get("customers_password"),
            customers_phone = request.POST.get("customers_phone"),
            customers_avatar = request.FILES.get("customers_avatar"),
        )
        customers_obj.save()
        return redirect("customers")  
    

class CustomersUpdateView(UpdateView):
    permission_required = ("customers.change_customers")

    model = Customers
    fields = [
        "customers_firstname","customers_middlename","customers_lastname","customers_username","customers_email",
        "customers_password","customers_phone","customers_avatar"
    ]
    template_name = "updatecustomers.html"
    def get_success_url(self):
        messages.success(self.request,"Customer Updated Succesfully..!")
        return reverse_lazy("customers")

    def get_context_data(self, **kwargs):
        # A function to init the global layout. It is defined in web_project/__init__.py file
        context = TemplateLayout.init(self, super().get_context_data(**kwargs))
        context['customers'] = self.get_customers(self.kwargs['pk'])
        return context
    def get_customers(self, pk):
        return Customers.objects.get(pk=pk)
    
class CustomersDeleteView(DeleteView):
    permission_required = ("customers.delete_customers")

        
    def get(self, request, pk):
        customers_obj = get_object_or_404(Customers, customers_id=pk)
        customers_obj.delete()
        messages.success(request, 'Record Deleted')
        return redirect('customers')

    