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
    # specific_store = "씨유신사드림점"
    # specific_store = (Store.objects.filter(
    #     store_name=specific_store))
    # print(specific_store[0].store_goods.all)  # store_goods
    # for s in specific_store[0].store_goods.all:
    #     print(s.goods_name)

    return render(request, 'main.html')


def deliver(request):
    stuffs = Delivery_my_stuff.objects.all()
    context = {
        "stuffs": stuffs,
    }
    return render(request, 'deliver.html', context)


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
    stores = Store.objects.all()
    context = {'stores': stores}
    store_name_list = []
    storeLat_in_total = []
    if request.is_ajax():
        storeLat_in_radius = request.GET.getlist('storeLat_in_radius[]')
        storeLang_in_radius = request.GET.getlist('storeLang_in_radius[]')
        # for (0 in range(0, len(storeLat_in_radius))):

        # storeLat_in_total = [storeLat_in_radius, storeLang_in_radius]
        print(storeLat_in_total)
        print(storeLat_in_radius)
        if(storeLat_in_radius):
            print("----")
            for storeLat, storeLang in zip(storeLat_in_radius, storeLang_in_radius):
                result_store_lat = (Store.objects.filter(
                    store_lat=storeLat, store_long=storeLang))
                result_store_lat = list(result_store_lat.values())
                store_name_list.append(result_store_lat[0]['store_name'])
            print(store_name_list)
            if(len(store_name_list) == 0):
                store_name_list = "등록된 가게가 없습니다."
                context = {'store_name_list': store_name_list}
            else:

                context = {'store_name_list': store_name_list}

            return HttpResponse(json.dumps(context), content_type='application/json')

    return render(request, 'request_market2.html', context)


def request_market_stuff(request):
    specific_good = []
    specific_price = []
    specific_category = []
    if request.is_ajax():
        specific_store_one = request.GET['specific_store_name']
        specific_store = (Store.objects.filter(
            store_name=specific_store_one))
        print(specific_store_one)
        specific_goods = specific_store[0].store_goods.all()
        print(specific_goods)
        for s in specific_goods:
            specific_good.append(s.goods_name)
            specific_price.append(s.goods_price)
            if(len(specific_category) == 0 or s.goods_category not in specific_category):
                specific_category.append(s.goods_category)
        print(specific_category)
        context = {'specific_good': specific_good,
                   'specific_price': specific_price,
                   'specific_category': specific_category,
                   'specific_store_one': specific_store_one}

        return HttpResponse(json.dumps(context), content_type='application/json')


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
