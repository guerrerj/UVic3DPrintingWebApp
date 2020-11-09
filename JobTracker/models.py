from django.db import models
from django.urls import reverse
from Login.models import Users

class Jobs(models.Model):
    jobId            = models.AutoField(primary_key=True)
    user             = models.ForeignKey(Users, verbose_name="Users", on_delete=models.CASCADE)
    cost             = models.DecimalField(max_digits=6, decimal_places=2)
    dateRequested    = models.DateTimeField(auto_now=False, auto_now_add=True)
    jobCompleted     = models.BooleanField(default=False)
    paymentCompleted = models.BooleanField(default=False)
    fileName         = models.FileField(upload_to='uploads/%Y/%m/%d/', max_length=100)
    jobDetails       = models.TextField()
    #jobTitle         = models.TextField(max_length=30)
    
    class Meta:
        """ Allows to define metadata for the database """
        ordering = ["-dateRequested"]
    
    def __str__(self):
        """ Lets us name instances of each record(row) """
        return str(self.jobId)
    
    def get_absolute_url(self):
        return reverse("jobs/view", kwargs={})
    