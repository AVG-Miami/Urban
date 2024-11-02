from django.shortcuts import render
from django.http import request
import requests
from django.http import HttpResponse


def login(request):
    return render(request, 'login.html')

def target(request):
    return render(request, 'OAuth.html')


def get_code(request):

    if request.GET.get('code') != None:
        print('')
        client_id = 'a4a6ed5d2d50408e8c73cc7445df4743'
        client_secret = '11b3b3bbd0f9478e8f5b2d44f69b962c'
        code = request.GET.get('code')

        # context = {
        #     'code': code,
        #     'client_id': client_id,
        #     'client_secret': client_secret,
        #     'ya_token': ya_token,
        #     }
#    return render(request, 'accounts/yandex/login/callback.html', context)
#        print(context)
        # Create your views here.
        url = "https://oauth.yandex.ru/token"

       # Учетные данные для API

        data = {
            'grant_type': 'authorization_code',
            'code': code,
            'client_id': client_id,
            'client_secret': client_secret,
            'redirect_uri': 'http://localhost:8000/accounts/yandex/login/callback.html/',  # Тот же URI, что и для запроса
            }
        print()
        print(data)
        # Отправьте POST-запрос

        response = requests.post(url, data=data)

        # Обработка ответа
        if response.status_code == 200:
            token_info = response.json()
            access_token = token_info.get("access_token")
            print(f"Мой Access Token: {access_token}")
            refresh_token = token_info.get("refresh_token")  # Если предоставляется

            url = "https://login.yandex.ru/info"
            headers = {
                      "Authorization": f"OAuth {access_token}",
                      }
            # Выполнение GET-запроса
            response = requests.get(url, headers=headers)
            # Обработка ответа
            if response.status_code == 200:
                user_info = response.json()
                print("Информация о пользователе:", user_info)
                # Логин пользователя можно получить из поля 'login'
                print("Логин:", user_info.get("login"))
                #return HttpResponse(f"Приветствуем, {user_info}!")
                context = {
                    'code': code,
                    'client_id': client_id,
                    'client_secret': client_secret,
                    'access_token': access_token,
                    'user_info': user_info
                    }
                return render(request, 'OAuth.html', context)
            else:
                print(f"Ошибка: {response.status_code}, {response.text}")

        else:
            print(f"Error: {response.status_code}, {response.text}")
