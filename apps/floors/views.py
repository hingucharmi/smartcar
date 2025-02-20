from django.contrib import messages
from django.views.generic import TemplateView , ListView , UpdateView,DeleteView
from web_project import TemplateLayout
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render , redirect
from apps.avenues.models import *
from apps.floors.models import *
from django.views import View
from django.urls import reverse_lazy

"""
This file is a view controller for multiple pages as a module.
Here you can override the page view layout.
Refer to academy/urls.py file for more pages.
"""
 # Predefined function


class FloorsView(TemplateView):
    template_name = "index_floors.html"

    def get_context_data(self, **kwargs):
        context = TemplateLayout.init(self, super().get_context_data(**kwargs))
        try:
            avenues_dict = AvenuesVO.objects.all()
            print(avenues_dict, "=====")
            context['avenues_dict'] = avenues_dict  # Add to context
        except Exception as e:
            print(f'{e} - Error while fetching AvenuesVO')
            context['avenues_dict'] = None  # Handle errors gracefully
        
        return context
    
   
class FloorsAddView(View):
    permission_required = ("floors.add_floors")

    def get_context_data(self, **kwargs):
        # A function to init the global layout. It is defined in web_project/__init__.py file
        context = TemplateLayout.init(self, super().get_context_data(**kwargs))

        return context
    def get(self, request):
        return render(request, "floors_add.html")  # Render form for new avenue

    def post(self, request):
        avenue = AvenuesVO.objects.get(avenues_id=request.POST.get("avenues_id"))
        floors_vo = FloorsVO(
            floors_name = request.POST.get("floors_name"),
            floors_slot_price = request.POST.get("floors_slot_price"),
            floors_plan = request.POST.get("floors_plan"),
            floors_avenues_id = avenue,
        )
        floors_vo.save()
        return redirect("floors")  # Redirect to list view after saving
    

    

class FloorsListView(ListView):
    model = FloorsVO ,AvenuesVO
    template_name = 'viewfloors.html'  # Template path

    def get_context_data(self, **kwargs):
        avenues_dict = AvenuesVO.objects.all()
        # A function to init the global layout. It is defined in web_project/__init__.py file
        context = TemplateLayout.init(self, super().get_context_data(**kwargs)) 
        try:
            floors_dict = FloorsVO.objects.all().order_by('floors_id')
            avenues_dict = AvenuesVO.objects.all()
            context['avenues_dict'] = avenues_dict  # Add to context
            context['floors_dict'] = floors_dict  # Add to context
        except Exception as e:
            print(f'{e} - Error while fetching AvenuesVO')
            context['avenues_dict'] = None  # Handle errors gracefully

        return context
    def get_queryset(self):   
           
        return FloorsVO.objects.all().order_by('floors_id')

class FloorsUpdateView(UpdateView):
    permission_required = ("floors.change_floors")

    model = FloorsVO
    fields = [
        "floors_name","floors_plan","floors_slot_price","floors_avenues_id",
    ]
    template_name = "updatefloors.html"
    def get_success_url(self):
        return reverse_lazy("floors")

    def get_context_data(self, **kwargs):
        # A function to init the global layout. It is defined in web_project/__init__.py file
        context = TemplateLayout.init(self, super().get_context_data(**kwargs))
        context['floors'] = self.get_floors(self.kwargs['pk'])
        context['avenues'] = AvenuesVO.objects.all()
        return context
    def get_floors(self, pk):
        return FloorsVO.objects.get(pk=pk)
    
class FloorsDeleteView(DeleteView):
    permission_required = ("floors.delete_floors")

    def get(self, request, pk):
        floors = get_object_or_404(FloorsVO, floors_id=pk)
        floors.delete()
        messages.success(request, 'Floors Deleted')
        return redirect('floors')
