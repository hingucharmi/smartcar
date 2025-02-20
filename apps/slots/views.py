from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.views.generic import TemplateView , ListView , DeleteView ,UpdateView
from django.contrib.auth.hashers import make_password
from web_project.template_helpers.theme import TemplateHelper
from web_project import TemplateLayout
from django.views import View
from apps.slots.models import SlotsVO
from django.db.models import Q
from apps.vendors.models import VendorVO
from apps.devices.models import DevicesVO
from apps.zones.models import ZonesVO
from apps.slots.forms import SlotsForm




class SlotsAddView(TemplateView):
    permission_required = ("slots.add_slots")

    def get_context_data(self, **kwargs):
        # A function to init the global layout. It is defined in web_project/__init__.py file
        context = TemplateLayout.init(self, super().get_context_data(**kwargs))

        return context
    def get(self, request):
        return render(request, "slots_list.html")  # Render form for new avenue

    def post(self, request):
        zones = ZonesVO.objects.get(zones_id=request.POST.get("zones_id"))
        vendors = VendorVO.objects.get(vendors_id=request.POST.get("vendors_id"))
        devices = DevicesVO.objects.get(devices_id=request.POST.get("devices_id"))

        slots = SlotsVO(
            slots_name = request.POST.get("slots_name"),
            slots_zones = zones,
            slots_vendors = vendors,
            slots_devices = devices,
            slots_price = request.POST.get("slots_price"),
            slots_status = request.POST.get("slots_status"),


        )
        slots.save()
        messages.success(request,'Add Slots Successfully..')
        return redirect("slots")  # Redirect to list view after saving
    

class SlotsListView(ListView):
    
    model = SlotsVO
    template_name = 'slots_list.html'  # Template path

    def get_context_data(self, **kwargs):
        vendors = VendorVO.objects.all()
        # A function to init the global layout. It is defined in web_project/__init__.py file
        context = TemplateLayout.init(self, super().get_context_data(**kwargs)) 
        try:
            slots_dict = SlotsVO.objects.all().order_by('slots_id')
            vendors_dict = VendorVO.objects.all()
            zones_dict = ZonesVO.objects.all()
            devices_dict = DevicesVO.objects.all()        
      
            context['slots_dict'] = slots_dict  # Add to context
            context['vendors_dict'] = vendors_dict  # Add to context
            context['zones_dict'] = zones_dict  # Add to context
            context['devices_dict'] = devices_dict  # Add to context
            print(context['devices_dict'],"context['devices_dict']")

        except Exception as e:

            print(f'{e} - Error while fetching vendors')
            context['slots_dict'] = None  # Handle errors gracefully

            
        return context
    def get_queryset(self):         
        return SlotsVO.objects.all().order_by('slots_id')


class SlotsUpdateView(UpdateView):
    permission_required = ("slots.change_slots")

    model = SlotsVO
    fields = [
        "slots_name","slots_vendors","slots_zones","slots_devices","slots_price","slots_status"
    ]
    template_name = "slots_update.html"

    def get_success_url(self):
        messages.success(self.request,'Slots Updated Succefully...')
        return reverse_lazy("slots")

    def get_context_data(self, **kwargs):
        # A function to init the global layout. It is defined in web_project/__init__.py file
        context = TemplateLayout.init(self, super().get_context_data(**kwargs))
        context['slots'] = self.get_slots(self.kwargs['pk'])
        context['vendors_dict'] = VendorVO.objects.all()
        context['devices_dict'] = DevicesVO.objects.all()
        context['zones_dict'] = ZonesVO.objects.all()
        return context
    
    def get_slots(self, pk):
        return SlotsVO.objects.get(pk=pk)
    

class SlotsDeleteView(DeleteView):
    permission_required = ("slots.delete_slots")
   
    
    def get(self, request, pk):
        slots = get_object_or_404(SlotsVO, slots_id=pk)
        slots.delete()
        messages.success(request, 'Slots Deleted')
        return redirect('slots')

