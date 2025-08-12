"""
URL configuration for templates project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.urls import path
from templateapp.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",index,name='index'),
    path("about/",about,name="about"), #static url
    path("contact/",contact,name="contact"),
    path("about-xyz-company",about,name='about'), #name space urls changes in html files using {% url 'about' %} depends on name for better modifying on url and to reuse the code again and again
    path("<int:id>/",dynamic_url,name='dynamic_url'),
    path('home/',HomeView.as_view(),name="home")

]
# static url and it is static we can't chnage for differnt companies so we now use namespace urls and it uses href in templates 
