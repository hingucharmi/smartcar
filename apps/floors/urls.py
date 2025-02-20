from django.urls import path
from .views import  FloorsListView , FloorsAddView ,FloorsDeleteView, FloorsUpdateView
from django.contrib.auth.decorators import login_required
from . import views
urlpatterns = [

    path(
        "floors/list/",
        login_required(FloorsListView.as_view(template_name="home.html")),name="floors"),
    path(
        "floors/add/",
        login_required(FloorsAddView.as_view()),name="floors_add"
        ),

    path("floors/update/<int:pk>/", 
         login_required(FloorsUpdateView.as_view()), name="floors_update"
         ),

    path (
        "floors/delete/<int:pk>/",
        login_required(FloorsDeleteView.as_view()), name="floors_delete"
        ),
    
    ]
