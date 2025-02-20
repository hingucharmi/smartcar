from django.urls import path
from .views import SlotsAddView , SlotsListView , SlotsDeleteView,SlotsUpdateView
from django.contrib.auth.decorators import login_required
from . import views

urlpatterns = [

    path(
        "slots/list/",
        login_required(SlotsListView.as_view(template_name="slots_list.html")),name="slots"),
    path(
        "slots/add/",
        login_required(SlotsAddView.as_view()),name="slots_add"
        ),

    path("slots/update/<int:pk>/", 
         login_required(SlotsUpdateView.as_view()), name="slots_update"
         ),

    path (
        "slots/delete/<int:pk>/",
        login_required(SlotsDeleteView.as_view()), name="slots_delete"
        ),
    
    ]
