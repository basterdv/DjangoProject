from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
# from exchange_things import views

from DjangoProject import settings

urlpatterns = [
    # path('', views.index, name='index'),
    path('', include('main.urls')),
    path('users/',include('users.urls')),
    path('goods/',include('goods.urls')),

    # path('advert/', views.advert, name='advert'),
    # path('advert_edit/', views.advert_edit, name='advert_edit')
    # path('exchange/', views.exchange, name='exchange'),
    path("admin/", admin.site.urls),
    path('orders/', include('orders.urls', namespace='orders')),
]

# if settings.DEBUG:
#     urlpatterns += [
#         path("__debug__/",include("debug_toolbar.urls")),
#         ]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


handler404 = 'main.views.custom_404_view'