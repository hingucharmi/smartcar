from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.views.generic import TemplateView , ListView , DeleteView ,UpdateView
from django.contrib.auth.hashers import make_password
from web_project.template_helpers.theme import TemplateHelper
from web_project import TemplateLayout
from django.views import View
from apps.vendors.models import VendorVO
from apps.vendors.forms import VendorsForm
from django.db.models import Q
from apps.avenues.models import AvenuesVO


class VendorsAddView(TemplateView):
    permission_required = ("vendors.add_vendors")

    def get_context_data(self, **kwargs):
        # A function to init the global layout. It is defined in web_project/__init__.py file
        context = TemplateLayout.init(self, super().get_context_data(**kwargs))

        return context
    def get(self, request):
        return render(request, "vendors_list.html")  # Render form for new avenue

    def post(self, request):
        avenues = AvenuesVO.objects.get(avenues_id=request.POST.get("avenues_id"))
        
        vendors = VendorVO(
            vendors_username = request.POST.get("vendors_username"),
            vendors_email = request.POST.get("vendors_email"),
            vendors_password = request.POST.get("vendors_password"),
            vendors_phone = request.POST.get("vendors_phone"),
            vendors_address = request.POST.get("vendors_address"),
            vendors_logo = request.FILES.get("vendors_logo"),
            vendors_avenues = avenues,


        )
        print(vendors.vendors_logo.name,"=====logo")
        vendors.save()
        messages.success(request,'Vendor Added...!')
        return redirect("vendors")  # Redirect to list view after saving
    

class VendorsListView(ListView):
    
    model = VendorVO
    template_name = 'vendors_list.html'  # Template path

    def get_context_data(self, **kwargs):
        vendors = VendorVO.objects.all()
        avenues_dict = AvenuesVO.objects.all()

        # A function to init the global layout. It is defined in web_project/__init__.py file
        context = TemplateLayout.init(self, super().get_context_data(**kwargs)) 
        try:
            vendors_dict = VendorVO.objects.all().order_by('vendors_id')
            avenues_dict = AvenuesVO.objects.all().order_by("avenues_id")

           
            print( vendors_dict ," vendors_dict")
            context['vendors_dict'] = vendors_dict  # Add to context
            context['avenues_dict'] = avenues_dict  # Add to context
            print(avenues_dict)
        except Exception as e:
            print(f'{e} - Error while fetching vendors')
            context['vendors_dict'] = None  # Handle errors gracefully

        return context
    
    def get_queryset(self):         
        return VendorVO.objects.all().order_by('vendors_id')


class VendorsUpdateView(UpdateView):
    permission_required = ("vendors.change_vendors")

    model = VendorVO
    fields = [
        "vendors_username", "vendors_email", "vendors_password","vendors_phone","vendors_address","vendors_logo","vendors_avenues"
    ]
    
    template_name = "vendors_update.html"
   
    def get_context_data(self, **kwargs):
        # A function to init the global layout. It is defined in web_project/__init__.py file
        context = TemplateLayout.init(self, super().get_context_data(**kwargs))
        context['vendors'] = self.get_vendors(self.kwargs['pk'])
        context['avenues_dict'] = AvenuesVO.objects.all()
      
        return context
    def post(self, request, pk):
        vendors = self.get_vendors(pk)
        form = VendorsForm(request.POST,request.FILES, instance=vendors)

        print("Received POST data:", request.POST)
        

        if form.is_valid():
            print("Form is valid!")
            print("Cleaned form data:", form.cleaned_data)

            if not self.vendors_exists(form.cleaned_data, vendors):
                vendor = form.save(commit=False)

                # Hash password if changed
                # if 'vendors_password' in form.cleaned_data and form.cleaned_data['vendors_password']:
                #     print("Updating password...")
                #     vendors.vendors_password = make_password(form.cleaned_data['vendors_password'])
                
                vendor.save()
                print("Vendor updated successfully:", vendor)
                messages.success(request, 'Vendor Updated')
            else:
                print("Vendor already exists!")
                messages.error(request, 'Vendor Already Exists')
        else:
            print("Form is invalid! Errors:", form.errors)
            messages.error(request, 'Vendor Update Failed: Invalid data')
        return redirect('vendors')
    
    def get_vendors(self, pk):
        print(VendorVO.objects.get(pk=pk),"here"),
        return VendorVO.objects.get(pk=pk)
    
    def vendors_exists(self, cleaned_data, current_vendors):
        matching_vendors = VendorVO.objects.filter(
            Q(vendors_username=cleaned_data['vendors_username']) &
            Q(vendors_email=cleaned_data['vendors_email']) &
            Q(vendors_password=cleaned_data['vendors_password']) &
            Q(vendors_phone=cleaned_data['vendors_phone']) &
            Q(vendors_address=cleaned_data['vendors_address'])&
            Q(vendors_logo=cleaned_data['vendors_logo'])
        ).exclude(pk=current_vendors.pk)
        return matching_vendors.exists()


class VendorsDeleteView(DeleteView):
    permission_required = ("vendors.delete_vendors")
   
    
    def get(self, request, pk):
        vendors = get_object_or_404(VendorVO, vendors_id=pk)
        vendors.delete()
        messages.success(request, 'Vendors Deleted')
        return redirect('vendors')

