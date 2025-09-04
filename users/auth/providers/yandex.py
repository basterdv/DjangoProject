import requests
from django.conf import settings


class YandexProvider:
    def get_auth_url(self):
        from urllib.parse import urlencode
        params = {
            'client_id': settings.OAUTH_PROVIDERS['yandex']['client_id'],
            'redirect_uri': settings.OAUTH_PROVIDERS['yandex']['redirect_uri'],
            'response_type': 'code',
            # 'scope': ' '.join(settings.OAUTH_PROVIDERS['yandex']['scopes'])
        }
        return f"https://oauth.yandex.ru/authorize?{urlencode(params)}"

    def get_user_info(self, code):

        # Обмен code на токен
        token_data = {
            'code': code,
            'client_id': settings.OAUTH_PROVIDERS['yandex']['client_id'],
            'client_secret': settings.OAUTH_PROVIDERS['yandex']['client_secret'],
            'grant_type': 'authorization_code'
        }


        token_url = settings.OAUTH_PROVIDERS['yandex']['token_url']

        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        token_response = requests.post(token_url, data=token_data, headers=headers)

        token_response.raise_for_status()
        access_token = token_response.json()['access_token']

        # Получение данных пользователя
        user_info_url =settings.OAUTH_PROVIDERS['yandex']['userinfo_url']

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


