"""core URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django import urls
from django.contrib import admin
from django.urls import path ,include # include ko import kea hai khud    

urlpatterns = [
    path('admin/', admin.site.urls),     
    path('api/', include('api.urls')),          #ye humne khud bnaya hai path is main puri app hogi           
                                
]
'''
    jab bhi project per kam krna hai tau app ka name settings.py main INSTALLED_APPS = ko btana hota hai
    iss project main hmari app ka name api hai    
    INSTALLED_APPS = main simple app ka name likhna hai bus 
    '''
#step1
# sb se phly hmara backend ka program core ke urls.py main hota hai.
# sub se pahly yahan per path dena hai .admin wala by default hota hai.
# humne apna path bnana hai jese 21 line per bnaya hai hmari puri app us main hogi.
# step 2 (urls.py api main hoga ab)


