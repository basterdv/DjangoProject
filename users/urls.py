from django.urls import path

from users import views
from users.views import Login, RegisterUserView, logout, PasswordReset,YandexOAuthView,OAuthCallbackView  # , Logout

app_name = 'users'

urlpatterns = [
    path('login/', Login.as_view(), name='login'),
    path('vk_auth_callback/', views.vk_auth_callback, name='vk_auth_callback'),
    path('yandex_auth_callback/', OAuthCallbackView.as_view() , name='yandex_auth_callback'),
    path('yandex_login/', YandexOAuthView.as_view(), name='yandex_login'),
    path('google_auth_callback/', views.google_auth_callback, name='google_auth_callback'),
    path('logout/', logout, name='logout'),
    path('registr/', RegisterUserView.as_view(), name='registration'),
    path('passwordreset/', PasswordReset.as_view(), name='password_reset'),
    path('profile/', views.profile, name='profile'),
]
