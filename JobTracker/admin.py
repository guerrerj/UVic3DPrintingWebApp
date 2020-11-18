from django.contrib import admin
from .models import Job, CustomUser

class JobsAdmin(admin.ModelAdmin):
    pass

class UsersAdmin(admin.ModelAdmin):
    pass

admin.site.register(Job, JobsAdmin)
admin.site.register(CustomUser, UsersAdmin)
