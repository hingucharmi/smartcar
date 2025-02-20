
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import TemplateView , ListView , DeleteView ,UpdateView
# from django.db.models import Sum
# from web_project.template_helpers.theme import TemplateHelper
from web_project import TemplateLayout
from django.views import View
from apps.avenues.models import AvenuesVO

class AvenuesAddView(TemplateView):

    permission_required = ("avenues.add_avenues")


    def get_context_data(self, **kwargs):
        # A function to init the global layout. It is defined in web_project/__init__.py file
        context = TemplateLayout.init(self, super().get_context_data(**kwargs))

        return context
    def get(self, request):
        return render(request, "viewavenues.html")  # Render form for new avenue

    def post(self, request):
        avenues = AvenuesVO(
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
        avenues.save()
        messages.success(request, 'Avenues Added')


        return redirect("avenues") # Redirect to list view after saving
    

class AvenuesListView(ListView):
    
    model = AvenuesVO
    template_name = 'viewavenues.html'  # Template path

    def get_context_data(self, **kwargs):
        avenues = AvenuesVO.objects.all()
        # A function to init the global layout. It is defined in web_project/__init__.py file
        context = TemplateLayout.init(self, super().get_context_data(**kwargs)) 
        try:
            avenues_dict = AvenuesVO.objects.all().order_by('avenues_id')
           
            context['avenues_dict'] = avenues_dict  # Add to context
           
        except Exception as e:
            print(f'{e} - Error while fetching AvenuesVO')
            context['avenues_dict'] = None  # Handle errors gracefully
        return context
    
    def get_queryset(self):         
        return AvenuesVO.objects.all().order_by('avenues_id')


class AvenuesUpdateView(UpdateView):

    permission_required = ("avenues.change_avenues")


    model = AvenuesVO
    fields = [
        "avenues_name", "avenues_username", "avenues_email", 
        "avenues_address", "avenues_slot_price", "avenues_logo", 
        "avenues_country", "avenues_state", "avenues_city", "avenues_pincode"
    ]
    
    template_name = "updateavenues.html"
    def get_success_url(self):
        messages.success(self.request, 'Avenues Updated Successfully.. ')
        return reverse_lazy("avenues")
                          
    def get_context_data(self, **kwargs):
        # A function to init the global layout. It is defined in web_project/__init__.py file
        context = TemplateLayout.init(self, super().get_context_data(**kwargs))
        context['avenues'] = self.get_avenues(self.kwargs['pk'])
        
        return context
    def get_avenues(self, pk):
        print("====",AvenuesVO.objects.get(pk=pk).pk)
        return AvenuesVO.objects.get(pk=pk)

class AvenuesDeleteView(DeleteView):
    permission_required = ("avenues.delete_avenues")
   
    
    def get(self, request, pk):
        avenues = get_object_or_404(AvenuesVO, avenues_id=pk)
        avenues.delete()
        messages.success(request, 'avenues Deleted')
        return redirect('avenues')
