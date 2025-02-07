"""PrintSystem URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path
from django.contrib.auth import views 
from django.conf.urls import include
from django.conf import settings 
from django.views.generic import RedirectView
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('', RedirectView.as_view(url="/jobs/view")),
    path('admin/', admin.site.urls),
    path('jobs/', include('JobTracker.urls')),
    path('accounts/', include('allauth.urls')),   
    path('payments/', include('payments.urls')),
    re_path(r'^.*/$', RedirectView.as_view(permanent=False, url="/"))
] 



if settings.DEBUG:
    # Test mode 
    from django.conf.urls.static import static
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)