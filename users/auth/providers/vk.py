import requests
from django.conf import settings
def vk_auth_callback(request):
    try:
        code = request.GET.get('code')
        device_id = request.GET.get('device_id')
        _type = request.GET.get('type')
        expires_in = request.GET.get('expires_in')
        # code_verifier = request.GET.get('code_verifier')
        state = request.GET.get('state')

        code_verifier = 'b5i9j_JQn3YeOlghVuS4WgdKcjoMIpJ7jFiOBO7QKSAxXa42HKu90hpMWQTL6F1KyoRrCD7Uw2H2u6mCQTJm-FMHro-NOYyhaPTsZqdkyFAvM85WGu0wa4g47SNOdyXW'

        TOKEN_EXCHANGE_URL = 'https://id.vk.com/oauth2/auth'
        USER_PUBLIC_DATA_EXCHANGE_URL = 'https://id.vk.com/oauth2/public_info'
        USER_INFO_DATA_EXCHANGE_URL = 'https://id.vk.com/oauth2/user_info'

        payload = {
            'grant_type': 'authorization_code',
            'client_id': 54015625,
            'device_id': device_id,
            'code': code,
            'redirect_uri': 'http://localhost/users/vk_auth_callback',
            'code_verifier': code_verifier,
            # 'state': state,

        }

        # Отправляем POST-запрос к VK API
        # print(payload)
        response = requests.post(TOKEN_EXCHANGE_URL, data=payload,
                                 headers={'Content-Type': 'application/x-www-form-urlencoded'})
        data = response.json()

        print(data)
        if 'access_token' in data:
            # print(response.json())
            access_token = data['access_token']
            id_token = data['id_token']
            expires_in = data['expires_in']
            # print(access_token)
            # print(id_token)
            # print(expires_in)

            # Отправляем POST-запрос для получения публичных данных пользователя
            payload = {
                'client_id': 54015625,
                'id_token': id_token,
            }

            response = requests.post(USER_PUBLIC_DATA_EXCHANGE_URL, data=payload,
                                     headers={'Content-Type': 'application/x-www-form-urlencoded'})
            data_user_public_info = response.json()
            # print(data_user_public_info)

            # Отправляем POST-запрос для получения личных данных пользователя
            payload = {
                'client_id': 54015625,
                'access_token': access_token,
            }

            response = requests.post(
                USER_INFO_DATA_EXCHANGE_URL,
                data=payload,
                headers={'Content-Type': 'application/x-www-form-urlencoded'}
            )
            data_user_info = response.json()
            # print(data_user_info)
            user_id = data_user_info['user']['user_id']
            email = data_user_info['user']['email']
            first_name = data_user_info['user']['first_name']
            last_name = data_user_info['user']['last_name']
            avatar = data_user_info['user']['avatar']
            birthday = data_user_info['user']['birthday']

            username = email
            # Поиск или создание пользователя в базе данных
            try:
                user = CustomUser.objects.get(email=email)
                logger.info(f'Пользователь с почтой {email} найден')
                # login(request, username) # Логинимся
            except:
                logger.error(f'Пользователь с потной {email} не найден')
                user = CustomUser.objects.create_user(
                    username=first_name,
                    email=email
                )
            # Логинимся
            user.first_name = first_name
            user.last_name = last_name
            user.avatar = avatar
            user.birthday = datetime.strptime(birthday, '%d.%m.%Y').date().strftime('%Y-%m-%d')

            user.username = first_name
            user.set_password(user_id)
            user.save()

            login(request, user)

        else:
            logger.error(f'error')

        template_name = 'users/vk_auth_callback.html'

        return render(request, template_name)
    except:
        template_name = 'users/login.html'
        logger.error(f'error')
        return render(request, template_name)


class VkProvider:
    def get_auth_url(self):
        from urllib.parse import urlencode
        params = {
            'client_id': 'b7986b6acead461082b4bbf881148c8f',
            # 'redirect_uri': 'https://yandex.ru/callback',
            'response_type': 'code',
            # 'scope': 'email',
        }

        return f"https://oauth.yandex.ru/authorize?{urlencode(params)}"

    def get_user_info(self, code):

        # Обмен code на токен
        token_data = {
            'code': code,
            'client_id': 'b7986b6acead461082b4bbf881148c8f',
            'client_secret': '389a4e23017e454eb8b5a03cb9ed0d16',
            'grant_type': 'authorization_code'
        }

        token_url = 'https://oauth.yandex.ru/token'
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        token_response = requests.post(token_url, data=token_data, headers=headers)

        token_response.raise_for_status()
        access_token = token_response.json()['access_token']

        # Получение данных пользователя
        user_info_url = 'https://login.yandex.ru/info'
        user_response = requests.get(user_info_url,
            headers={'Authorization': f'OAuth {access_token}'}
        )

        user_response.raise_for_status()

        return {
            'id': user_response.json()['id'],
            'email': user_response.json()['default_email'],
            'first_name': user_response.json()['first_name'],
            'last_name': user_response.json()['last_name'],
            'default_avatar_id': user_response.json()['default_avatar_id'],
            'login': user_response.json().get('login', ''),
            'birthday': user_response.json()['birthday'],
        }


