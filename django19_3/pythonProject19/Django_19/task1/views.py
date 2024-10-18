from django.shortcuts import render
from .UserRegister import UserRegister
from django.http import HttpResponse
from .models import *

def main(request):
    return render(request,'fourth_task/main.html')

def magazine(request):
#    games =[]  # ['Atomic Heart','Cyberpunk 2077','PayDay 2']
    games = Game.objects.all()
    # for game in new_games:
    #     games.append(str(game))
    context = {
        'games': games
    }
    return render(request,'fourth_task/magazine.html', context)

def corzine(request):
    return render(request,'fourth_task/corzine.html')

# def sign_up_by_django(requset):
#     users = ['Andy','Alex','Piter','Nick']
#
#     info = {}
#     context = {}
#     if requset.method == 'POST':
#         form = UserRegister(requset.POST)
#         if form.is_valid():
#             username = form.cleaned_data['username']
#             password = form.cleaned_data['password']
#             repeat_password = form.cleaned_data['repeat_password']
#             age = form.cleaned_data['age']
#
#             print('django запрос')
#             print(f"username : {username}")
#             print(f"password : {password}")
#             print(f"repeat_password : {repeat_password}")
#             print(f"age : {age}")
#             if password != repeat_password:
#                 info = {'error': 'Пароли не совпадают'}
#                 print('no pass')
#             elif int(age) < 18:
#                 info = {'error': 'Вы должны быть старше 18'}
#             elif username in users:
#                 info = {'error': 'Пользователь уже существует'}
#             else:
#                 return HttpResponse(f"Приветствуем, {username}!")
#     else:
#         form = UserRegister()
#     context = {'form': form,
#                }
#     context.update(info)
#     return render(requset,'fifth_task/registration_page.html', context)

def sign_up_by_html(requset):
    users = []
    buyers = Buyer.objects.all()
    for user in buyers:
        users.append(str(user))

    info = {}
    if requset.method == 'POST':
        username = requset.POST.get('username')
        password = requset.POST.get('password')
        repeat_password = requset.POST.get('repeat_password')
        age = requset.POST.get('age')
        print('html запрос')
        print(f"username : {username}")
        print(f"password : {password}")
        print(f"repeat_password : {repeat_password}")
        print(f"age : {age}")

        if password != repeat_password:
            info = {'error': 'Пароли не совпадают'}
            print('no pass')
        elif int(age) < 18:
            info = {'error': 'Вы должны быть старше 18'}
        elif username in users:
            info = {'error': 'Пользователь уже существует'}
        else:
            buyers.create (name=username, age=age, balance = 0 )
            return HttpResponse(f"Приветствуем, {username}!")
    context = info
    return render(requset,'fifth_task/registration_page.html', context)