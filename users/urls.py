from django.urls import path, include

from users import views
from users.views import Login, RegisterUserView, profile, logout, PasswordReset,VKAuthView  # , Logout

app_name = 'users'

# urlpatterns = [
#     path('login/', views.login, name='login'),
#     path('registration/', views.registration, name='registration'),
#     path('profile/', views.profile, name='profile'),
#     # path('users-cart/',views.users_cart,name='users_cart'),
#     path('logout/', views.logout, name='logout'),]

urlpatterns = [
    path('login/', Login.as_view(), name='login'),
    # path('login_vk_redirect/', Login.as_view(), name='login_vk_redirect'),
    # path('vk_auth_start/', views.vk_auth_start, name='vk_auth_start'),
    path('vk_auth_callback/', views.vk_auth_callback, name='vk_auth_callback'),
    # path('vk_auth_callback/',VKAuthView.as_view(), name='vk_auth_callback'),
    path('google_auth_callback/', views.google_auth_callback, name='google_auth_callback'),
    path('logout/', logout, name='logout'),
    path('registr/', RegisterUserView.as_view(), name='registration'),
    path('passwordreset/', PasswordReset.as_view(), name='password_reset'),
    path('profile/', views.profile, name='profile'),
]
