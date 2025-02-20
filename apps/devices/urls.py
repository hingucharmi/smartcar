from django.urls import path
from .views import DevicesAddView , DevicesListView , DevicesDeleteView,DevicesUpdateView
from django.contrib.auth.decorators import login_required
from . import views

urlpatterns = [

    path(
        "devices/list/",
        login_required(DevicesListView.as_view(template_name="devices_list.html")),name="devices"),
    path(
        "devices/add/",
        login_required(DevicesAddView.as_view()),name="devices_add"
        ),

    path("devices/update/<int:pk>/", 
         login_required(DevicesUpdateView.as_view()), name="devices_update"
         ),

    path (
        "devices/delete/<int:pk>/",
        login_required(DevicesDeleteView.as_view()), name="devices_delete"
        ),
    
    ]
