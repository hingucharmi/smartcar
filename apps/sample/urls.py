from django.urls import path
from .views import SampleView
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path(
        "",
        login_required(SampleView.as_view(template_name="index.html")),
        name="index",
    ),
    path(
        "page_2/",
        login_required(SampleView.as_view(template_name="page_2.html")),
        name="page-2",
    ),
]
