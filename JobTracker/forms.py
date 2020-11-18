from django.forms import ModelForm
from allauth.account.forms import SignupForm
from django import forms
from .models import Job, CustomUser

class JobForm(ModelForm):    
    class Meta:
        model = Job
        verbose_name = "Job List"
        fields = ["projectTitle", "fileName", "jobDetails"]


class CustomSignupForm(SignupForm):
    studentId = forms.CharField(max_length=10, required=True)
    def save(self, request):
        user = super(CustomSignupForm, self).save(request) 
        user.studentId = self.cleaned_data['studentId']
        user.save()
        return user 
    