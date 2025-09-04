from datetime import datetime
import requests
from django.conf import settings


class VkProvider:
    def get_auth_url(self):
        from urllib.parse import urlencode
        params = {
            'client_id': settings.OAUTH_PROVIDERS['vk']['client_id'],
            'redirect_uri': settings.OAUTH_PROVIDERS['vk']['redirect_uri'],
            'response_type': 'code',
            'code_challenge': settings.OAUTH_PROVIDERS['vk']['code_challenge'],
            'code_challenge_method': 's256',
            'scope': (''.join(settings.OAUTH_PROVIDERS['vk']['scope']))
        }

        return f"{settings.OAUTH_PROVIDERS['vk']['authorize_url']}?{urlencode(params)}"

    def get_user_info(self, code, device_id):
        # Обмен code на токен
        token_data = {
            'grant_type': 'authorization_code',
            'client_id': settings.OAUTH_PROVIDERS['vk']['client_id'],
            'code': code,
            'device_id': device_id,
            'redirect_uri': settings.OAUTH_PROVIDERS['vk']['redirect_uri'],
            'code_verifier': settings.OAUTH_PROVIDERS['vk']['code_verifier'],
        }

        # Отправляем POST-запрос к VK API
        token_url = settings.OAUTH_PROVIDERS['vk']['token_url']
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        token_response = requests.post(token_url, data=token_data, headers=headers)

        token_response.raise_for_status()

        access_token = token_response.json()['access_token']
        id_token = token_response.json()['id_token']

        # Получение данных пользователя
        payload = {
            'client_id': settings.OAUTH_PROVIDERS['vk']['client_id'],
            'access_token': access_token,
        }
        public_payload = {
            'client_id': settings.OAUTH_PROVIDERS['vk']['client_id'],
            'id_token': id_token,
        }

        user_info_url = settings.OAUTH_PROVIDERS['vk']['userinfo_url']
        public_info_url = settings.OAUTH_PROVIDERS['vk']['public_info']

        user_response = requests.post(user_info_url, data=payload,
                                      headers={'Content-Type': 'application/x-www-form-urlencoded'}
                                      )
        user_response_public = requests.post(public_info_url, data=public_payload,
                                             headers={'Content-Type': 'application/x-www-form-urlencoded'}
                                             )

        user_response.raise_for_status()

        user_birthday = datetime.strptime(user_response.json()['user']['birthday'], '%d.%m.%Y').date().strftime(
            '%Y-%m-%d')

        return {
            'id': user_response.json()['user']['user_id'],
            'email': user_response.json()['user']['email'],
            'first_name': user_response.json()['user']['first_name'],
            'last_name': user_response.json()['user']['last_name'],
            'avatar_id': user_response.json()['user']['avatar'],
            'birthday': user_birthday,
            'login': user_response.json()['user']['first_name']
        }
