from django.views.generic import TemplateView , ListView , UpdateView,DeleteView
from web_project import TemplateLayout
from django.http import HttpResponse
from django.shortcuts import render , redirect
from apps.avenues.models import *
from django.views import View
from django.urls import reverse_lazy

"""
This file is a view controller for multiple pages as a module.
Here you can override the page view layout.
Refer to academy/urls.py file for more pages.
"""
 # Predefined function


class AvenuesListView(ListView):
    model = AvenuesVO
    template_name = 'viewavenues.html'  # Template path
    context_object_name = 'avenues_dict'
    def get_context_data(self, **kwargs):
        # A function to init the global layout. It is defined in web_project/__init__.py file
        context = TemplateLayout.init(self, super().get_context_data(**kwargs))

        return context
    def get_queryset(self):
        return AvenuesVO.objects.all().order_by('avenues_id')

class AvenuesView(TemplateView):
    # Predefined function
    def get_context_data(self, **kwargs):
        # A function to init the global layout. It is defined in web_project/__init__.py file
        context = TemplateLayout.init(self, super().get_context_data(**kwargs))

        return context


    def index(request):
        try:
            return render(request, "home.html")

        except Exception as e:
            print(f'{e} coming error')

    def load_avenues(request):
        try:
            return render(request, "index.html")
        except Exception as e:
            print(f'{e} coming error')

    def edit_avenues(request):
        avenues_id = request.GET.get("avenues_id")
        avenues_dict = AvenuesVO.objects.filter(avenues_id = avenues_id).all()
        return render(request, 'updateavenues.html',{'avenues_dict' : avenues_dict})


    # def update_avenues(request):
    #     avenues_id = request.POST.get("avenues_id")
    #     avenues_name = request.POST.get("avenues_name")
    #     avenues_username = request.POST.get("avenues_username")
    #     avenues_email = request.POST.get("avenues_email")
    #     avenues_password = request.POST.get("avenues_password")
    #     avenues_address = request.POST.get("avenues_address")
    #     avenues_slot_price = request.POST.get("avenues_slot_price")
    #     avenues_logo = request.POST.get("avenues_logo")
    #     avenues_country = request.POST.get("avenues_country")
    #     avenues_state = request.POST.get("avenues_state")
    #     avenues_city = request.POST.get("avenues_city")
    #     avenues_pincode = request.POST.get("avenues_pincode")

    #     print("address======",avenues_address)
    #     avenues_vo = AvenuesVO()

    #     avenues_vo.avenues_id = avenues_id
    #     avenues_vo.avenues_name =  avenues_name
    #     avenues_vo.avenues_username = avenues_username
    #     avenues_vo.avenues_email = avenues_email
    #     avenues_vo.avenues_password = avenues_password
    #     avenues_vo.avenues_address = avenues_address
    #     avenues_vo.avenues_slot_price = avenues_slot_price
    #     avenues_vo.avenues_logo = avenues_logo
    #     avenues_vo.avenues_country = avenues_country
    #     avenues_vo.avenues_state = avenues_state
    #     avenues_vo.avenues_city = avenues_city
    #     avenues_vo.avenues_pincode = avenues_pincode

    #     avenues_vo.save()

    #     return render(request,"home.html")


class AvenuesEditView(UpdateView):
    model = AvenuesVO
    template_name = "updateavenues.html"

    def get_context_data(self,  request, *args,**kwargs):
        avenues_id = kwargs.get('avenues_id')
        print(avenues_id,"avenues_id")
        avenues_dict = AvenuesVO.objects.filter(avenues_id=avenues_id).first()

        context = TemplateLayout.init(self, super().get_context_data(**kwargs))

        return render(request, self.template_name, {'avenues_dict': avenues_dict},context,)
    

class AvenuesUpdateView(UpdateView):
    model = AvenuesVO
    fields = [
        "avenues_name", "avenues_username", "avenues_email", 
        "avenues_address", "avenues_slot_price", "avenues_logo", 
        "avenues_country", "avenues_state", "avenues_city", "avenues_pincode"
    ]
    template_name = "updateavenues.html"
    def get_success_url(self):
        return reverse_lazy("avenues")

    def get_context_data(self, **kwargs):
        # A function to init the global layout. It is defined in web_project/__init__.py file
        context = TemplateLayout.init(self, super().get_context_data(**kwargs))
        return context
    
class AvenuesDeleteView(DeleteView):
    model = AvenuesVO
    template_name = 'confirm_delete.html'  # Custom template name
    
    def get_success_url(self):
        return reverse_lazy('avenues')
    def get_context_data(self, **kwargs):
        # A function to init the global layout. It is defined in web_project/__init__.py file
        context = TemplateLayout.init(self, super().get_context_data(**kwargs))

        return context
        
    
class AvenueCreateView(View):
    def get_context_data(self, **kwargs):
        # A function to init the global layout. It is defined in web_project/__init__.py file
        context = TemplateLayout.init(self, super().get_context_data(**kwargs))

        return context
    def get(self, request):
        return render(request, "index1.html")  # Render form for new avenue

    def post(self, request):
        avenues_vo = AvenuesVO(
            avenues_name=request.POST.get("avenues_name"),
            avenues_username=request.POST.get("avenues_username"),
            avenues_email=request.POST.get("avenues_email"),
            avenues_password=request.POST.get("avenues_password"),
            avenues_address=request.POST.get("avenues_address"),
            avenues_slot_price=request.POST.get("avenues_slot_price"),
            avenues_logo=request.POST.get("avenues_logo"),
            avenues_country=request.POST.get("avenues_country"),
            avenues_state=request.POST.get("avenues_state"),
            avenues_city=request.POST.get("avenues_city"),
            avenues_pincode=request.POST.get("avenues_pincode"),
        )
        avenues_vo.save()
        return redirect("avenues")  # Redirect to list view after saving
    