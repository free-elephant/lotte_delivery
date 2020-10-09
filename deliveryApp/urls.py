from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('deliver/', views.deliver, name="deliver"),
    path('request/', views.request, name="request"),
    path('request2/', views.request2, name="request2"),
    path('request_candidate/', views.request_candidate, name="request_candidate"),
    path('changeradius/', views.changeradius, name='changeradius'),
]
