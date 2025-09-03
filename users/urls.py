from django.urls import path

from users import views
from users.views import Login, RegisterUserView, logout, PasswordReset  # , Logout

app_name = 'users'

urlpatterns = [
    path('login/', Login.as_view(), name='login'),
    path('vk_auth_callback/', views.vk_auth_callback, name='vk_auth_callback'),
    path('yandex_auth_callback/', views.yandex_auth_callback, name='yandex_auth_callback'),
    path('google_auth_callback/', views.google_auth_callback, name='google_auth_callback'),
    path('logout/', logout, name='logout'),
    path('registr/', RegisterUserView.as_view(), name='registration'),
    path('passwordreset/', PasswordReset.as_view(), name='password_reset'),
    path('profile/', views.profile, name='profile'),
]
