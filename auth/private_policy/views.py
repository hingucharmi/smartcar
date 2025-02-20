from django.shortcuts import get_object_or_404, redirect, render
from django.contrib import messages
from django.urls import reverse_lazy
from auth.views import AuthView

from web_project import TemplateLayout
from django.views import View

class PrivatePolicy(AuthView):

    def get(self, request):
        if request.user.is_authenticated:
            # If the user is already logged in, redirect them to the home page or another appropriate page.
            return redirect("avenues")  # Replace 'index' with the actual URL name for the home page

        # Render the login page for users who are not logged in.
        return super().get(request)
    
    def get(self, request):
        return render(request, "auth/privatepolicy.html")  # Render form for new avenue
    
class PrivatePolicyView(AuthView):
    def get(self, request):
        # Render the login page for users who are not logged in.
        return super().get(request)


    