from django.urls import path
from .views import Login, RegisterUser, profile,logout #, Logout

urlpatterns = [
    path('login/', Login.as_view(), name='login'),
    # path('logout/', Logout.as_view(), name='logout'),
    path('logout/', logout, name='logout'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('profile/', profile, name='profile'),
]