from django.urls import path
from apps.customers.views import CustomersListView ,CustomersAddView , CustomersDeleteView ,CustomersUpdateView
from django.contrib.auth.decorators import login_required


urlpatterns = [
    
    path("customers/list",login_required(CustomersListView.as_view()),name="customers"),

    path("customers/add",login_required(CustomersAddView.as_view()),name="add_customers"),

    path("customers/delete/<int:pk>/",login_required(CustomersDeleteView.as_view()),
         name="customers_delete"),
    
    path("customers/update/<int:pk>/",login_required(CustomersUpdateView.as_view()),
         name="customers_update"),

]
