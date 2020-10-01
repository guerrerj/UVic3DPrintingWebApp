from django.contrib import admin
from .models import Users 

class LoginAdmin(admin.ModelAdmin):
    pass 

admin.site.register(Users, LoginAdmin) 

