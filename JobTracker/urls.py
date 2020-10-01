from django.urls import path 
from .views import AboutView, JobsListView, JobsCreateView 

urlpatterns = [
    path('about/', AboutView.as_view(), name="about"),
    path('view/', JobsListView.as_view(), name="view"),
    path('create/', JobsCreateView.as_view(), name="create")
]