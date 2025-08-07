from django.urls import path, include

from users import views
from users.views import Login, RegisterUserView, profile, logout, PasswordReset  # , Logout

app_name = 'users'

# urlpatterns = [
#     path('login/', views.login, name='login'),
#     path('registration/', views.registration, name='registration'),
#     path('profile/', views.profile, name='profile'),
#     # path('users-cart/',views.users_cart,name='users_cart'),
#     path('logout/', views.logout, name='logout'),]

urlpatterns = [
    path('login/', Login.as_view(), name='login'),

    path('login_vk/', include('social_django.urls', namespace='social',)),
    # path('logout/', Logout.as_view(), name='logout'),
    path('logout/', logout, name='logout'),
    path('registr/', RegisterUserView.as_view(), name='registration'),
    path('passwordreset/', PasswordReset.as_view(), name='password_reset'),
    path('profile/', views.profile, name='profile'),
]
