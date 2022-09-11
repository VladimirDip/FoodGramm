from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from foodgramm_base import settings

handler400 = 'foodgramm_base.views.page_bad_request'
handler404 = 'foodgramm_base.views.page_not_found'
handler500 = 'foodgramm_base.views.server_error'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('django.contrib.auth.urls')),
    path('auth/', include('users.urls')),
    path('api/', include('api.urls')),
    path('', include('recipes.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)