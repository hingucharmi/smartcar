from django.urls import path
from .views import SubscriptionsAddView , SubscriptionsListView , SubscriptionsDeleteView,SubscriptionsUpdateView
from django.contrib.auth.decorators import login_required
from . import views

urlpatterns = [

    path(
        "subscriptions/list/",
        login_required(SubscriptionsListView.as_view(template_name="subscriptionlist.html")),name="subscriptions"),

    path(
        "subscriptions/add/",
        login_required(SubscriptionsAddView.as_view()),name="subscriptions_add"
        ),

    path("subscriptions/update/<int:pk>/", 
         login_required(SubscriptionsUpdateView.as_view()), name="subscriptions_update"
         ),

    path (
        "subscriptions/delete/<int:pk>/",
        login_required(SubscriptionsDeleteView.as_view()), name="subscriptions_delete"
        ),
    
    ]
