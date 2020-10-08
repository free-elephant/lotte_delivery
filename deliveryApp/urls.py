from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('deliver/', views.deliver, name="deliver"),
    path('request/', views.request, name="request"),

]
