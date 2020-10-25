from django.shortcuts import render, redirect, get_object_or_404, redirect
from django.http import HttpResponseRedirect, JsonResponse, HttpResponse
from django.contrib import auth

from django.contrib.auth.models import User
from django.utils import timezone
from .models import Delivery_my_stuff
from .models import Delivery_market

from storeApp.models import Goods, Store
from accountApp.models import Player

import json, math


def main(request):
    if(request.user.username == "admin"):
        auth.logout(request)
        print("관리자계정이면 로그아웃")
        return redirect('/')

    return render(request, 'main.html')


def deliver(request):
    stuffs = Delivery_my_stuff.objects.all()
    markets = Delivery_market.objects.all()
    context = {
        "stuffs": stuffs,
        "markets": markets
    }
    return render(request, 'deliver.html', context)

def deliverItem(request):
    if request.method=="GET":
        return render(request, 'deliver.html')
    elif request.method=="POST":
        position = request.POST['hiddenPosition'].split(',')
        position[0]=position[0][0:9]
        position[1]=position[1][0:10]
        position[2]=position[2][0:9]
        position[3]=position[3][0:10]
        print(position[0])
        print(position[1])
        print(position[2])
        print(position[3])
        d_stuff = Delivery_my_stuff.objects.get(my_departure_lat = position[0])
        d_stuff.deliver_stuff_user = request.user
        d_stuff.save()
        return redirect('/')
        
def request_my(request):
    if request.method == "GET":
        return render(request, 'request_my.html')
    elif request.method == "POST":
        d_stuff = Delivery_my_stuff()
        d_stuff.stuff_user = request.user
        d_stuff.my_departure_lat = request.POST['deparature_lat']  # 위도
        d_stuff.my_departure_long = request.POST['deparature_long']
        d_stuff.my_departure_address = request.POST['deparature']
        d_stuff.my_departure_addr = request.POST['deparature_detail']
        d_stuff.my_departure_phone = request.POST['deparature_phone']

        d_stuff.my_destination_lat = request.POST['destination_lat']
        d_stuff.my_destination_long = request.POST['destination_long']
        d_stuff.my_destination_address = request.POST['destination']
        d_stuff.my_destination_addr = request.POST['destination_detail']
        d_stuff.my_destination_phone = request.POST['destination_phone']

        d_stuff.my_date = request.POST['want_date']
        d_stuff.my_time = request.POST['want_time']
        d_stuff.my_created = timezone.datetime.now()
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
    print
    store_name_list = []
    storeLat_in_total = []
    if request.is_ajax():
        storeLat_in_radius = request.GET.getlist('storeLat_in_radius[]')
        print(storeLat_in_radius)
        storeLang_in_radius = request.GET.getlist('storeLang_in_radius[]')

        print(storeLat_in_total)
        print(storeLat_in_radius)
        if(storeLat_in_radius):
            print("----")
            for storeLat, storeLang in zip(storeLat_in_radius, storeLang_in_radius):

                result_store_lat = (Store.objects.filter(
                    store_lat=storeLat, store_lng=storeLang))
                result_store_lat = list(result_store_lat.values())
                store_name_list.append(result_store_lat[0]['store_name'])
            print(store_name_list)
            if(len(store_name_list) == 0):
                store_name_list = "등록된 가게가 없습니다."
                context = {'store_name_list': store_name_list}
            else:
                context = {'store_name_list': store_name_list}

            return HttpResponse(json.dumps(context), content_type='application/json')

    return render(request, 'request_market2.html', {'stores': stores})


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


def request_market_purchase(request):
    order = []
    order_lst = []  # market, stuff, count 분리된 것을 list에 넣어주기

    # store_lat_list = []  # 위도
    # store_lng_list = []  # 경도
    total_price = 0  # 전체 가격
    total_weigth = 0  # 전체 무게
    if request.method == "POST":
        order_total = request.POST['order_total']
        orders = order_total.split(',')
        print(orders)
        for order in orders:
            market, stuff, count = order.split('-')
            temp_lst = [market, stuff, count]
            order_lst.append(temp_lst)

            # 마켓 위도 경도 구하기
            # order_market_one = Store.objects.filter(
            #     store_name=market)
            # for m in order_market_one:
            #     store_lat_list.append(m.store_lat)
            #     store_lng_list.append(m.store_lng)

            # stuff 값에 접근해서 알아내기 - 가격, 무게 계산
            specific_stuff = Goods.objects.filter(
                goods_name=stuff)
            for i in specific_stuff:
                i.goods_price = i.goods_price * int(count)
                i.goods_weight = i.goods_weight * int(count)
                total_price += i.goods_price
                total_weigth += i.goods_weight

            # 무게 계산
        print(total_price)
        print(total_weigth)

        context = {
            'order_total': order_total,
            'order_lst': order_lst,
            'total_price': total_price,
            'total_weigth': total_weigth

        }
        return render(request, 'request_market_purchase.html', context)
    return render(request, 'request_market2.html')


def request_market_complete(request):
    purchase = []
    purchase_total = []
    if request.method == "POST":
        delivery = Delivery_market()  # db 생성
        delivery.mar_user = request.user
        purchase_total = request.POST['purchase_total']

        purchase = purchase_total.split(',')
        print(purchase)
        market_overlap_check = []  # 똑같은 마켓일 경우 알기 위함- 이미 안에 있다면, 아이템 추가
        for thing in purchase:
            market, stuff, count = thing.split('-')
            market_query = Store.objects.filter(
                store_name=market)
            if(market not in market_overlap_check):
                for m in market_query:
                    if(len(market_overlap_check) == 0):

                        delivery.mar_departure_lat = m.store_lat
                        delivery.mar_departure_long = m.store_lng
                        delivery.mar_departure_addr = market
                        delivery.mar_departure_phone = 123123
                        delivery.mar_item = stuff
                        delivery.mar_count = count

                        market_overlap_check.append(market)
                    elif(len(market_overlap_check) == 1):
                        delivery.mar1_departure_lat = m.store_lat
                        delivery.mar1_departure_long = m.store_lng
                        delivery.mar1_departure_addr = market
                        delivery.mar1_departure_phone = 123123
                        delivery.mar1_item = stuff
                        delivery.mar1_count = count

                        market_overlap_check.append(market)
                    elif(len(market_overlap_check) == 2):
                        delivery.mar2_departure_lat = m.store_lat
                        delivery.mar2_departure_long = m.store_lng
                        delivery.mar2_departure_addr = market
                        delivery.mar2_departure_phone = 123123

                        market_overlap_check.append(market)
                    elif(len(market_overlap_check) == 3):
                        delivery.mar3_departure_lat = m.store_lat
                        delivery.mar3_departure_long = m.store_lng
                        delivery.mar3_departure_addr = market
                        delivery.mar3_departure_phone = 123123

                        market_overlap_check.append(market)
            else:  # 이미 이름이 있는 경우
                print('1')
                if(market_overlap_check.index(market) == 0):
                    print('2')
                    delivery.mar_item = delivery.mar_item+','+stuff
                    delivery.mar_count = delivery.mar_count + ','+count
                elif(market_overlap_check.index(market) == 1):
                    print('3')
                    delivery.mar1_item = delivery.mar_item+','+stuff
                    delivery.mar1_count = delivery.mar_count + ','+count
                elif(market_overlap_check.index(market) == 2):
                    print('4')
                    delivery.mar2_item = delivery.mar_item+','+stuff
                    delivery.mar2_count = delivery.mar_count + ','+count
                elif(market_overlap_check.index(market) == 3):
                    print('5')
                    delivery.ma3_item = delivery.mar_item+','+stuff
                    delivery.mar3_count = delivery.mar_count + ','+count

            delivery.mar_destination_lat = request.POST['destination_lat']
            # destination_detail/destination_phone/mar_time
            delivery.mar_destination_long = request.POST['destination_long']
            delivery.mar_destination_addr = request.POST['destination_detail']
            delivery.mar_destination_phone = request.POST['destination_phone']
            delivery.mar_time = request.POST['want_time']  # 시간 설정ㅇ
            delivery.mar_weight = request.POST['total_weight']
            delivery.mar_price = request.POST['total_price']
            delivery.mar_distance = 123
            delivery.mar_content = request.POST['content']
            delivery.save()

    # for i in range(0, len(purchase_total)):
    #     print(purchase_total[i][0])
    # purchase_things = purchase_total.split(',')
    # print(purchase_total)
    # for thing in purchase_things:
    #     market, stuff, count = thing.split('-')
    #     temp_list = [market, stuff, count]
    #     purchase.append(temp_list)
    #     print

        return redirect('/')


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
