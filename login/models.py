from django.db import models

class Users(models.Model):
    username    = models.CharField(max_length=60)
    user        = models.EmailField(max_length=254) # This is the email
    studentID   = models.CharField(max_length=10)
    password    = models.CharField(max_length=50)
    createdDate = models.DateTimeField(auto_now=False, auto_now_add=True)
    lastAccessDate  = models.DateTimeField(auto_now=False, auto_now_add=False)
    isAdminUser = models.BooleanField(False)
    
    class Meta:
        ordering =["-username"]
    
    def __str__(self):
        """ Allows admin to view username as objects  """
        return self.username
