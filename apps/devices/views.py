from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.views.generic import TemplateView , ListView , DeleteView ,UpdateView
from django.contrib.auth.hashers import make_password
from web_project.template_helpers.theme import TemplateHelper
from web_project import TemplateLayout
from django.views import View
from apps.devices.models import DevicesVO
from apps.devices.forms import DevicesForm
from django.db.models import Q

from apps.avenues.models import AvenuesVO
from apps.vendors.models import VendorVO

class DevicesAddView(TemplateView):
    permission_required = ("devices.add_devices")

    def get_context_data(self, **kwargs):
        # A function to init the global layout. It is defined in web_project/__init__.py file
        context = TemplateLayout.init(self, super().get_context_data(**kwargs))

        return context
    def get(self, request):
        return render(request, "devices_list.html")  # Render form for new avenue

    def post(self, request):
        avenues = AvenuesVO.objects.get(avenues_id=request.POST.get("avenues_id"))
        vendors = VendorVO.objects.get(vendors_id=request.POST.get("vendors_id"))
        devices = DevicesVO(
            devices_name = request.POST.get("devices_name"),
            devices_mac = request.POST.get("devices_mac"),
            devices_type = request.POST.get("devices_type"),
            devices_avenues = avenues,
            devices_vendors = vendors,
            devices_image = request.POST.get("devices_image"),
            devices_state = request.POST.get("devices_state"),
            devices_status = request.POST.get("devices_status"),
        )
        devices.save()
        return redirect("devices")  # Redirect to list view after saving
    

class DevicesListView(ListView):
    
    model = DevicesVO
    template_name = 'devices_list.html'  # Template path

   
    def get_context_data(self, **kwargs):
        avenues_dict = AvenuesVO.objects.all()
        vendors_dict = VendorVO.objects.all()

        # A function to init the global layout. It is defined in web_project/__init__.py file
        context = TemplateLayout.init(self, super().get_context_data(**kwargs))

        try:
            avenues_dict = AvenuesVO.objects.all().order_by("avenues_id")
            vendors_dict = VendorVO.objects.all()
            devices_dict = DevicesVO.objects.all()
            # print(customers_dict )
            # print(subscriptions_dict)
            # print(subscriptionsplan_dict  )
            context['devices_dict'] = devices_dict  # Add to context
            context['vendors_dict'] = vendors_dict  # Add to context
            context['avenues_dict'] = avenues_dict  # Add to context
        except Exception as e:
            print(f'{e} - Error while fetching subscriptions')
            context['devices_dict'] = None,
            context['vendors_dict'] = None ,
            context['avenues_dict'] = None
        return context
    
    def get_queryset(self):             
        return DevicesVO.objects.all().order_by('devices_id')


class DevicesUpdateView(UpdateView):
    permission_required = ("devices.change_devices")

    model = DevicesVO
    fields = [
        "devices_name", "devices_mac", "devices_type","devices_image","devices_state","devices_status","devices_avenues",
        "devices_vendors"
    ]
    
    template_name = "devices_update.html"
   
    def get_success_url(self):
        messages.success(self.request,"Devices Updated Successfully...!")
        return reverse_lazy("devices")

    def get_context_data(self, **kwargs):
        # A function to init the global layout. It is defined in web_project/__init__.py file
        context = TemplateLayout.init(self, super().get_context_data(**kwargs))
        context['devices'] = self.get_devices(self.kwargs['pk'])
        context['avenues_dict'] = AvenuesVO.objects.all()
        context['vendors_dict'] = VendorVO.objects.all()

        return context
    def get_devices(self, pk):
        return DevicesVO.objects.get(pk=pk)
    

class DevicesDeleteView(DeleteView):
    permission_required = ("devices.delete_devices")
   
    
    def get(self, request, pk):
        devices = get_object_or_404(DevicesVO, devices_id=pk)
        devices.delete()
        messages.success(request, 'devices Deleted')
        return redirect('devices')

