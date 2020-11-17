from django.views.generic import TemplateView 
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect 
from django.shortcuts import render 
from django.shortcuts import redirect 
from django.views import View 
from django.views.generic import ListView, CreateView

from .models import Job, CustomUser
from .forms import JobForm


class AboutView(TemplateView):
    template_name = "about.html"

class JobsListView(ListView):
    template_name = "viewjobs.html"
    context_object_name = "jobs"      
    model = Job 
    
    # return only the user's requests if they don't have admin privilege 
    def get_queryset(self):
        user = list(CustomUser.objects.filter(username=self.request.user))[0] 
        # If the user has isAdminUser then return all the requests for viewing 
        if user.isAdminUser:
            return  Job.objects.all().order_by('dateRequested')
        else:
           return Job.objects.filter(user=self.request.user).order_by('dateRequested')
    
    
class JobsCreateView(CreateView):
    form_class = JobForm
    template_name = "createjob.html"
    context_object_name = "jobs"

