from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, JsonResponse
from django.contrib import auth

from django.utils import timezone
from .models import Delivery_my_stuff


def main(request):
    if(request.user.username == "admin"):
        auth.logout(request)
        print("관리자계정이면 로그아웃")
        return redirect('/')
    return render(request, 'main.html')


def deliver(request):
    return render(request, 'deliver.html')


def request(request):
    if request.method == "GET":
        return render(request, 'request.html')
    elif request.method == "POST":
        d_stuff = Delivery_my_stuff()
        d_stuff.my_departure_lat = request.POST['deparature_lat']  # 위도
        d_stuff.my_departure_long = request.POST['deparature_long']
        d_stuff.my_departure_addr = request.POST['deparature_detail']
        d_stuff.my_departure_phone = request.POST['deparature_phone']

        d_stuff.my_destination_lat = request.POST['destination_lat']
        d_stuff.my_destination_long = request.POST['destination_long']
        d_stuff.my_destination_addr = request.POST['destination_detail']
        d_stuff.my_destination_phone = request.POST['destination_phone']

        d_stuff.my_created = timezone.datetime.now()
        d_stuff.my_limit_time = request.POST['time']
        d_stuff.my_goods = request.POST['goods_category_one']
        d_stuff.my_goodsinfo = request.POST['goods_detail']

        d_stuff.my_weigth = request.POST['weight']
        d_stuff.my_distance = request.POST['distance']
        d_stuff.my_price = request.POST['price']
        d_stuff.my_content = request.POST['comment']
        d_stuff.save()
        return redirect('/')


def request2(request):
    return render(request, 'request2.html')


def request_candidate(request):
    return render(request, 'request_candidate.html')


def changeradius(request):
    radius = request.GET['select_radius']
    result = {
        'result': 'success',
        'radius': radius
    }
    return JsonResponse(result)
