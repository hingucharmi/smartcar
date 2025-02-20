from django.urls import path
from .views import ZonesAddView , ZonesListView , ZonesDeleteView,ZonesUpdateView
from django.contrib.auth.decorators import login_required
from . import views

urlpatterns = [

    path(
        "zones/list/",
        login_required(ZonesListView.as_view(template_name="zones_list.html")),name="zones"),
    path(
        "zones/add",
        login_required(ZonesAddView.as_view()),name="zones_add"
        ),

    path("zones/update/<int:pk>/", 
         login_required(ZonesUpdateView.as_view()), name="zones_update"
         ),

    path (
        "zones/delete/<int:pk>/",
        login_required(ZonesDeleteView.as_view()), name="zones_delete"
        ),
    
    ]
