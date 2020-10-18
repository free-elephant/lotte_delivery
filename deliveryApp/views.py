from django.shortcuts import render, redirect, get_object_or_404, redirect
from django.http import HttpResponseRedirect, JsonResponse, HttpResponse
from django.contrib import auth

from django.utils import timezone
from .models import Delivery_my_stuff

from storeApp.models import Goods, Store

import json


def main(request):
    if(request.user.username == "admin"):
        auth.logout(request)
        print("관리자계정이면 로그아웃")
        return redirect('/')
    return render(request, 'main.html')


def deliver(request):
    return render(request, 'deliver.html')


def request_my(request):
    if request.method == "GET":
        return render(request, 'request_my.html')
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

        d_stuff.my_date = request.POST['want_date']
        d_stuff.my_time = request.POST['want_time']
        d_stuff.my_created = timezone.datetime.now()
        d_stuff.my_limit_time = request.POST['limited_time']
        d_stuff.my_goods = request.POST['goods_category_one']
        d_stuff.my_goodsinfo = request.POST['goods_detail']

        d_stuff.my_weigth = request.POST['weight']
        d_stuff.my_distance = request.POST['distance']
        d_stuff.my_price = request.POST['price']
        d_stuff.my_content = request.POST['comment']
        d_stuff.save()
        return redirect('/')


def request_market2(request):
    return render(request, 'request_market2.html')


def request_market(request):
    store = Store.objects.all()
    goods_checked = []
    print("in")
    if request.method == "POST":
        #     print("in")
        #     market = request.POST['store']
        #     goods_checked = request.POST['goods_checked']
        #     print(goods_checked)
        #     context={'market':market,'goods_checked':goods_checked}
        return render(request, 'request_market.html')
    # if request.is_ajax():
    #     result_store_name=[]
    #     search_word = request.GET['search_word']
    #     print(search_word)
    #     if search_word:
    #         print('inininin')
    #         result_store = Store.objects.filter(
    #             store_name__icontains=search_word)
    #         print(result_store)
    #         result_store=list(result_store.values())

    #         for i in range(0,len(result_store)):
    #             result_store_name.append(result_store[i]['store_name'])

    #         print(result_store_name)

    #         if(len(result_store_name) == 0):
    #             result_store_name = "등록된 카멧이 없습니다."
    #             context = {'result_store': result_store}
    #         else:

    #             context = {'result_store': result_store_name}

    #     return HttpResponse(json.dumps(context), content_type='application/json')
    return render(request, 'request_market.html', {'store': store})


def market(request):
    store = Store.objects.all()
    if request.method == "POST":
        market_search_word = request.POST['market_search_q']
        if market_search_word:
            result_store = Store.objects.filter(
                store_name__icontains=market_search_word)
            return render(request, 'market.html', {'store': store, 'result_store': result_store})
    return render(request, 'market.html', {'store': store})


def market_detail(request, store_id):
    store = get_object_or_404(Store, pk=store_id)
    context = {'store': store}
    return render(request, 'market_detail.html', context)


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
