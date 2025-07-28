from django.urls import path

from users import views

from django.urls import path
from users.views import Login, RegisterUser, profile, logout  # , Logout

app_name = 'users'

# urlpatterns = [
#     path('login/', views.login, name='login'),
#     path('registration/', views.registration, name='registration'),
#     path('profile/', views.profile, name='profile'),
#     # path('users-cart/',views.users_cart,name='users_cart'),
#     path('logout/', views.logout, name='logout'),]

urlpatterns = [
    path('login/', Login.as_view(), name='login'),
    # path('logout/', Logout.as_view(), name='logout'),
    path('logout/', logout, name='logout'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('profile/',views.profile, name='profile'),
]
