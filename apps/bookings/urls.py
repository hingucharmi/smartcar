from django.urls import path
from .views import BookingsAddView , BookingsListView , BookingsUpdateView ,BookingsDeleteView
from django.contrib.auth.decorators import login_required
from . import views

urlpatterns = [

    path(
        "bookings/list/",
        login_required(BookingsListView.as_view(template_name="bookings_list.html")),name="bookings"),
    path(
        "bookings/add/",
        login_required(BookingsAddView.as_view()),name="bookings_add"
        ),

    path("bookings/update/<int:pk>/", 
         login_required(BookingsUpdateView.as_view()), name="bookings_update"
         ),

    path (
        "bookings/delete/<int:pk>/",
        login_required(BookingsDeleteView.as_view()), name="bookings_delete"
        ),
    
    ]
