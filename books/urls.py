from django.contrib import admin 
from django.urls import path, include 
from register import views

urlpatterns = [ 
	path('admin/', admin.site.urls), 
    path("register/", views.register, name="register"),  
	path('', include('booksapp.urls')),
	path('', include("django.contrib.auth.urls")), 

] 
