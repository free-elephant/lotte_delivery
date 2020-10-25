from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, JsonResponse
from django.contrib import auth
# Create your views here.


def signup(request):
    if request.method == 'POST':
        if request.POST['password1'] == request.POST['password2']:
            user = User.objects.create_user(
                username=request.POST['id'],
                password=request.POST['password1'],
                email=request.POST['email']
            )
            user.player.player_name = request.POST['name']
            user.player.player_phone = request.POST['phone']
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
    if request.method == 'POST':
        auth.logout(request)
        return redirect('/')
    return render(request, 'signup.html')


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
    return render(request, 'info.html')
