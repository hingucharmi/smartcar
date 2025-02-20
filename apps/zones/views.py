
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import TemplateView , ListView , DeleteView ,UpdateView
from django.db.models import Sum
from web_project.template_helpers.theme import TemplateHelper
from web_project import TemplateLayout
from django.views import View
from apps.zones.models import ZonesVO
from apps.floors.models import FloorsVO

class ZonesAddView(TemplateView):
    permission_required = ("zones.add_zones")

    def get_context_data(self, **kwargs):
        # A function to init the global layout. It is defined in web_project/__init__.py file
        context = TemplateLayout.init(self, super().get_context_data(**kwargs))

        return context
    def get(self, request):
        return render(request, "zones_list.html")  # Render form for new avenue

    def post(self, request):
        floors = FloorsVO.objects.get(floors_id=request.POST.get("floors_id"))
        zones = ZonesVO(
            zones_name = request.POST.get("zones_name"),
            zones_capacity = request.POST.get("zones_capacity"),
            zones_slot_price = request.POST.get("zones_slot_price"),
            zones_floors_id = floors,

        )
        zones.save()
        messages.success(request,'Zones Added Succeffully..!')
        return redirect("zones")  # Redirect to list view after saving
    

class ZonesListView(ListView):
    
    model = ZonesVO , FloorsVO
    template_name = 'zones_list.html'  # Template path

    def get_context_data(self, **kwargs):
        zones = ZonesVO.objects.all()
        # A function to init the global layout. It is defined in web_project/__init__.py file
        context = TemplateLayout.init(self, super().get_context_data(**kwargs)) 
        try:
            zones_dict = ZonesVO.objects.all().order_by('zones_id')
            floors_dict = FloorsVO.objects.all()
            print( floors_dict ," floors_dict")
            context['zones_dict'] = zones_dict  # Add to context
            context['floors_dict'] = floors_dict
        except Exception as e:
            print(f'{e} - Error while fetching AvenuesVO')
            context['zones_dict'] = None  # Handle errors gracefully

            

        return context
    def get_queryset(self):         
        return ZonesVO.objects.all().order_by('zones_id')


class ZonesUpdateView(UpdateView):
    permission_required = ("zones.change_zones")

    model = ZonesVO
    fields = [
        "zones_name", "zones_floors_id", "zones_slot_price","zones_capacity"
    ]
    
    template_name = "zones_update.html"
    def get_success_url(self):
        messages.success(self.request,'Zones Updated Succefully...!')
        return reverse_lazy("zones")

    def get_context_data(self, **kwargs):
        # A function to init the global layout. It is defined in web_project/__init__.py file
        context = TemplateLayout.init(self, super().get_context_data(**kwargs))
        context['zones'] = self.get_zones(self.kwargs['pk'])
        context['floors'] = FloorsVO.objects.all()
        return context
    def get_zones(self, pk):
        print("====",ZonesVO.objects.get(pk=pk).pk)
        return ZonesVO.objects.get(pk=pk)

class ZonesDeleteView(DeleteView):
    permission_required = ("zones.delete_zones")
   
    
    def get(self, request, pk):
        zones = get_object_or_404(ZonesVO, zones_id=pk)
        zones.delete()
        messages.success(request, 'Zones Deleted')
        return redirect('zones')
