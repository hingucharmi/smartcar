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
from apps.customers.models import Customers
from apps.slots.models import SlotsVO
from apps.bookings.models import BookingVO



class BookingsAddView(TemplateView):

    permission_required = ("bookings.add_bookings")

    def get_context_data(self, **kwargs):
        # A function to init the global layout. It is defined in web_project/__init__.py file
        context = TemplateLayout.init(self, super().get_context_data(**kwargs))

        return context
    def get(self, request):
        return render(request, "bookings_list.html")  # Render form for new avenue

    def post(self, request):
        customers = Customers.objects.get(customers_id=request.POST.get("customers_id"))
        slots = SlotsVO.objects.get(slots_id=request.POST.get("slots_id"))
      
        bookings = BookingVO(
            bookings_customers = customers,
            bookings_slots = slots,
            bookings_price = request.POST.get("bookings_price"),
            start_date = request.POST.get("start_date"),
            end_date = request.POST.get("end_date"),
           
        )
        bookings.save()
        messages.success(request, 'Bookings Added Successfully...')

        return redirect("bookings")  # Redirect to list view after saving
    

class BookingsListView(ListView):
    
    model = BookingVO
    template_name = 'bookings_list.html'  # Template path

    def get_context_data(self, **kwargs):
        # A function to init the global layout. It is defined in web_project/__init__.py file
        context = TemplateLayout.init(self, super().get_context_data(**kwargs)) 
        try:

            booking = BookingVO.objects.first()
           
            
            bookings_dict = BookingVO.objects.all().order_by('bookings_id')
            customers_dict = Customers.objects.all()
            slots_dict = SlotsVO.objects.all()
            
            context['bookings_dict'] = bookings_dict  # Add to context
            context['customers_dict'] = customers_dict  # Add to context
            context['slots_dict'] = slots_dict  # Add to context
            
            print(context['bookings_dict'],"context['bookings_dict']")

        except Exception as e:
            print(f'{e} - Error while fetching Bookings')
            context['bookings_dict'] = None  # Handle errors gracefully
        return context
    
    def get_queryset(self):         
        return BookingVO.objects.all().order_by('bookings_id')


class BookingsUpdateView(UpdateView):
   
    permission_required = ("bookings.change_bookings")
   

    model = BookingVO
    fields = [
        "bookings_customers","bookings_slots","bookings_price","start_date","end_date"
    ]
    template_name = "bookings_update.html"

    def get_success_url(self):
        messages.success(self.request, 'Bookings Updated Successfully...!')

        return reverse_lazy("bookings")

    def get_context_data(self, **kwargs):
        # A function to init the global layout. It is defined in web_project/__init__.py file
        context = TemplateLayout.init(self, super().get_context_data(**kwargs))
        context['bookings'] = self.get_slots(self.kwargs['pk'])
        context['customers_dict'] = Customers.objects.all()
        context['slots_dict'] = SlotsVO.objects.all()
        return context
    
    def get_slots(self, pk):
        print("reached here")
        return BookingVO.objects.get(pk=pk)
    

class BookingsDeleteView(DeleteView):
   
    permission_required = ("bookings.delete_bookings")

    
    def get(self, request, pk):
        bookings = get_object_or_404(BookingVO, bookings_id=pk)
        bookings.delete()
        messages.success(request, 'Bookings Deleted')
        return redirect('bookings')

