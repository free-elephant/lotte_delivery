from deliveryApp.models import Delivery_my_stuff
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, JsonResponse, HttpResponse
from django.contrib import auth
import sys
import os
import json
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
# Create your views here.


def signup(request):
    if request.method == 'POST':
        if request.POST['password1'] == request.POST['password2']:
            user = User.objects.create_user(
                username=request.POST['id_1'],
                password=request.POST['password1'],
                # email=request.POST['email']
            )
            user.player.player_name = request.POST['name']
            # user.player.player_phone = request.POST['phone']
            auth.login(request, user)
            return redirect('/')
    return render(request, 'signup.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['id']
        password = request.POST['password']
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            return render(request, 'login.html', {'error': '아이디 혹은 비밀번호가 틀림'})
    else:
        return render(request, 'login.html')


def logout(request):
    # if request.method == 'POST':
    auth.logout(request)
    return redirect('/')
    # return redirect('/')


def idcheck(request):
    try:
        user = User.objects.get(username=request.GET['id'])
    except Exception as e:
        user = None

    result = {
        'result': 'success',
        'data': "not exist" if user is None else "exist"
    }
    return JsonResponse(result)


def info(request):
    user = User.objects.filter(
        username=request.user.username)
    deliver_list = Delivery_my_stuff.objects.filter(
        deliver_stuff_user__in=user)  # 내가 배달한 경우
    delivered_list = Delivery_my_stuff.objects.filter(
        stuff_user__in=user)  # 내가 배달 요청한 경우

    context = {
        'user': user,
        'deliver_list': deliver_list,
        'delivered_list': delivered_list,
    }

    return render(request, 'info.html', context)


def delete_delivered(request, delivered_id):
    delivered_d = get_object_or_404(
        Delivery_my_stuff, pk=delivered_id)  # 특정 객체 가져오기(없으면 404 에러)
    delivered_d.delete()
    return redirect("/")
