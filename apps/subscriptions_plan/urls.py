from django.urls import path
from django.contrib.auth.decorators import login_required
from apps.subscriptions_plan.subscriptions_plan_list.views import SubscriptionsPlanListView
from apps.subscriptions_plan.subscriptions_plan_add.views import SubscriptionsPlanAddView
from apps.subscriptions_plan.subscriptions_plan_update.views import SubscriptionPlanUpdateView
from apps.subscriptions_plan.subscriptions_plan_delete.views import SubscriptionsPlanDeleteView
from uuid import UUID 


urlpatterns = [
    path(
        "subscriptionplan/list/",
        login_required(SubscriptionsPlanListView.as_view(template_name="subscriptions_plan_list.html")),
        name="subscriptionsplan",
    ),
    path(
        "subscriptionplan/add/",
        login_required(SubscriptionsPlanAddView.as_view()),
        name="add_subscriptionsplan",
    ),
    path (
        "subscriptionplan/update/<int:pk>/",
        login_required(SubscriptionPlanUpdateView.as_view(template_name='subscriptions_plan_update.html')),
        name="update_subscriptionsplan",
    ),
    path (
        "subscriptionplan/delete/<int:pk>/",
        login_required(SubscriptionsPlanDeleteView.as_view()),
        name="delete_subscriptionsplan",
    ),

]