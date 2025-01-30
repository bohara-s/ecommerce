"""
URL configuration for e_commerce project.

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
from django.urls import path,include
from django.http import HttpResponse
from .view import home,product,contact,feedback

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home,name="home"),
    path('product/',product,name='product'),
    path('contact/', contact,name='contact'),
    path('feedback/', feedback, name='feedback'),
    path('account/',include('account.urls'))
    # path('login/', login, name='login'), 
    # Add this URL pattern for login page
    
    # Add a new URL pattern for feedback page
    # Add a new URL pattern for contact page
    # Add more URL patterns here if needed
]
