from django.urls import path 
from .views import AboutView, JobsListView, JobsCreateView 
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('about/', login_required(AboutView.as_view()), name="about"),
    path('view/', login_required(JobsListView.as_view()), name="view"),
    path('create/', login_required(JobsCreateView.as_view()), name="create")
]