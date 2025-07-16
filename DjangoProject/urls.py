from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from exchange_things import views
# from DjangoProject import settings

urlpatterns = [
    path('', views.index, name='index'),
    path('users/',include('exchange_things.urls')),
    # path('sign_in/', views.sign_in, name='sign_in'),
    # path('register/', views.register, name='register'),
    path('advert/', views.advert, name='advert'),
    # path('accounts/', views.account, name='accounts'),
    path('exchange/', views.exchange, name='exchange'),
    path("admin/", admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += [
        path("__debug__/",include("debug_toolbar.urls")),
        ]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = 'exchange_things.views.custom_404_view'