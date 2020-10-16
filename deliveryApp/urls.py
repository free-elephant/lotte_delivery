from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('deliver/', views.deliver, name="deliver"),
    path('request_my/', views.request_my, name="request_my"),
    path('request_market/', views.request_market, name="request_market"),
    path('request2/', views.request2, name="request2"),
    path('request_candidate/', views.request_candidate, name="request_candidate"),

    path('market/', views.market, name="market"),
    path('market_detail/<int:store_id>', views.market_detail, name="market_detail"),

    path('changeradius/', views.changeradius, name='changeradius'),
]
