from django.urls import path

from users import views
from users.views import Login, RegisterUserView, logout, PasswordReset, YandexOAuthView, VKOAuthView, \
    OAuthCallbackView

app_name = 'users'

urlpatterns = [
    path('login/', Login.as_view(), name='login'),
    path('auth_callback/<str:provider>', OAuthCallbackView.as_view(), name='auth_callback'),
    # path('vk_auth_callback/', OAuthCallbackView.as_view(),{'provider':'vk'}, name='vk_auth_callback'),
    path('yandex_login/', YandexOAuthView.as_view(), name='yandex_login'),
    path('vk_login/', VKOAuthView.as_view(), name='vk_login'),
    path('logout/', logout, name='logout'),
    path('registr/', RegisterUserView.as_view(), name='registration'),
    path('passwordreset/', PasswordReset.as_view(), name='password_reset'),
    path('profile/', views.profile, name='profile'),
]
