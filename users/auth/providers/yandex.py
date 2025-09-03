import requests
from django.conf import settings


class YandexProvider:
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


