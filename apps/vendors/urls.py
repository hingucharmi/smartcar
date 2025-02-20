from django.urls import path
from .views import VendorsAddView , VendorsListView , VendorsDeleteView,VendorsUpdateView
from django.contrib.auth.decorators import login_required
from . import views

urlpatterns = [

    path(
        "vendors/list/",
        login_required(VendorsListView.as_view(template_name="vendors_list.html")),name="vendors"),
    path(
        "vendors/add/",
        login_required(VendorsAddView.as_view()),name="vendors_add"
        ),

    path("vendors/update/<int:pk>/", 
         login_required(VendorsUpdateView.as_view()), name="vendors_update"
         ),

    path (
        "vendors/delete/<int:pk>/",
        login_required(VendorsDeleteView.as_view()), name="vendors_delete"
        ),
    
    ]
