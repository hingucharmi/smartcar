from django.urls import path
from .views import AvenuesDeleteView,AvenuesListView, AvenuesUpdateView, AvenuesAddView
from django.contrib.auth.decorators import login_required
from . import views

urlpatterns = [
     path(
        "app/avenues/",
        login_required(AvenuesListView.as_view(template_name="viewavenues.html")),name="avenues"),
    path(
        "avenues/add/",
        login_required(AvenuesAddView.as_view()),name="avenues_add"
        ),

    path("avenues/update/<int:pk>/", 
         login_required(AvenuesUpdateView.as_view()), name="avenues_update"
         ),

    path (
        "avenues/delete/<int:pk>/",
        login_required(AvenuesDeleteView.as_view()), name="avenues_delete"
        ),

   
]
