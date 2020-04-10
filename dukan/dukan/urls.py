"""
Definition of urls for dukan.
"""

from datetime import datetime
from django.urls import path
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from app import forms, views

"""URL connecting to views...."""
urlpatterns = [
    path('', views.home, name='home'),
    path('contact/', views.contact, name='contact'),
    path('contact/<str:customer_name>/', views.contact, name='contact'),
    path('about/<str:customer_name>/', views.about, name='about'),
    path('about/', views.about, name='about'),
    path('register/', views.register, name='register'),
    path('loginshop/', views.loginShop, name='loginShop'),
    path('logincust/', views.logincust, name='logincust'),
    path('detail/<str:customer_name>/', views.detail, name='detail'),
    path('detail/', views.detail, name='detail'),
    path('update/<str:shop_name>/', views.update, name='update'),
    path('update/', views.update, name='update'),
    path('book/<str:customer_name>/', views.book, name='book'),
    path('photo/',views.photo, name='photo'),
    path('admin/', admin.site.urls)
]
