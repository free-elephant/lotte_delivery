from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('deliver/', views.deliver, name="deliver"),
    path('deliverItem/', views.deliverItem, name="deliverItem"),
    path('request_my/', views.request_my, name="request_my"),
    path('request_market/', views.request_market, name="request_market"),
    path('request_market2/', views.request_market2, name="request_market2"),
    path('request_market_stuff/', views.request_market_stuff,name="request_market_stuff"),

    path('request_market_purchase/', views.request_market_purchase,
         name="request_market_purchase"),
    path('request_market_complete/', views.request_market_complete,
         name="request_market_complete"),

    path('request2/', views.request2, name="request2"),
    path('request_candidate/', views.request_candidate, name="request_candidate"),


    path('market/', views.market, name="market"),
    path('market_detail/<int:store_id>',
         views.market_detail, name="market_detail"),

    path('changeradius/', views.changeradius, name='changeradius'),
]
