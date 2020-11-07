from django.views.generic import TemplateView 
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect 
from django.shortcuts import render 
from django.shortcuts import redirect 
from django.views import View 
from django.views.generic import ListView, CreateView

from .models import Job
from .forms import JobForm


class AboutView(TemplateView):
    template_name = "about.html"

class JobsListView(ListView):
    template_name = "viewjobs.html"
    context_object_name = "jobs"
    queryset = Job.objects.all() 
    model = Job 
    
class JobsCreateView(CreateView):
    form_class = JobForm
    template_name = "createjob.html"
    context_object_name = "jobs"

