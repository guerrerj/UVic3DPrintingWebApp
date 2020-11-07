from django.db import models
from django.urls import reverse
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):    
    userId        = models.AutoField(primary_key=True)
    createdDate = models.DateTimeField(auto_now=False, auto_now_add=True)
    lastAccessDate  = models.DateTimeField(auto_now=True, auto_now_add=False)
    isAdminUser = models.BooleanField(default=False)
    studentId = models.CharField(max_length=10)
    
    class Meta:
        ordering =["-username"]
        verbose_name = 'User'
    
    # def __str__(self):
    #     """ Allows admin to view username as objects  """
    #     return self.username
# To sync db -> python manage.py migrate --run-syncdb
#Manually delete migrations folder, delete sqlite3 then run makemigrations then migrate 

class Job(models.Model):
    jobId            = models.AutoField(primary_key=True)
    user             = models.ForeignKey(CustomUser, verbose_name="User", on_delete=models.CASCADE)
    cost             = models.DecimalField(max_digits=6, decimal_places=2)
    dateRequested    = models.DateTimeField(auto_now=False, auto_now_add=True)
    jobCompleted     = models.BooleanField(default=False)
    paymentCompleted = models.BooleanField(default=False)
    fileName         = models.FileField(upload_to='uploads/%Y/%m/%d/', max_length=100)
    jobDetails       = models.TextField()
    
    class Meta:
        """ Allows to define metadata for the database """
        ordering = ["-dateRequested"]
        db_table = 'Job'
        verbose_name = "Job List"
    
    def __str__(self):
        """ Lets us name instances of each record(row) """
        return str(self.jobId)
    
    def get_absolute_url(self):
        return reverse("jobs/view", kwargs={})
