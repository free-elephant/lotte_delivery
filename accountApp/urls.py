from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('idcheck/', views.idcheck, name='idcheck'),
    path('info/', views.info, name='info'),
    path('delete_deliverd/<int:delivered_id>',
         views.delete_delivered, name="delete_delivered"),
]
