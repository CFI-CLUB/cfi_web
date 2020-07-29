from django.contrib import admin
from django.urls import path, include
from django.conf.urls import handler404
from django.conf import settings
from django.conf.urls.static import static

handler404 = 'club.views.handler404'


urlpatterns = [
    path('admin/', admin.site.urls),
    path('cfi/', include('cfi.urls')),
    path('club/', include('club.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



