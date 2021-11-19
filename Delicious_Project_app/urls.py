#copied from urls.py of project

from django.contrib import admin
from django.urls import path
from Delicious_Project_app import views

urlpatterns = [
    
    path('', views.Home, name='Home'),
    path("about" , views.about, name='About'),
    path("order" , views.order, name='Order'),
    path("userlogin" , views.userlogin, name='Login'),
    path("handlesignup" , views.handlesignup, name='SignUp'),
    path("logout" , views.userlogout, name='LogOut'),
]