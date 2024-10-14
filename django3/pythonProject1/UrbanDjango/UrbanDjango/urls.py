"""
URL configuration for UrbanDjango project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from example1.views import index
# from example1.views import index2
from  django.views.generic import TemplateView
from task2.views import class_view, func_view
from task3.views import main, magazine, corzine

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',main),
    path('magazine/', magazine),
    path('corzine/', corzine)

#    path('index/', TemplateView.as_view(template_name='index2.html'))

    ]