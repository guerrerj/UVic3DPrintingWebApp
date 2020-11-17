from django.views.generic import TemplateView 
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect 
from django.shortcuts import render 
from django.shortcuts import redirect 
from django.views import View 
from django.views.generic import ListView, CreateView

from .models import Job, CustomUser
from .forms import JobForm
"""
from .models import Author
"""

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
            return  Job.objects.all().order_by('-dateRequested')
        else:
           return Job.objects.filter(user=self.request.user).order_by('-dateRequested')
    
    
class JobsCreateView(CreateView):
    form_class = JobForm
    template_name = "createjob.html"
    context_object_name = "jobs"

"""
class AuthorCreate(CreateView):
    model = Author
    fields = ['name']

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)
"""
def add_job(request):
    #print(request.POST)
    projtitle = request.POST["projectTitle"]
    filnam = request.POST["fileName"]
    jobdet = request.POST["jobDetails"]
    created_obj = Job.objects.create(projectTitle=projtitle, fileName=filnam, jobDetails=jobdet, cost=0.00, user=request.user)
    #print(created_obj)
    #length_of_jobs = Job.objects.all().count()
    #print(length_of_jobs)
    return(redirect('/jobs/view'))