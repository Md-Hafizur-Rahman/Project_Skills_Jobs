from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('app/', include('apps.frontend.urls')),
    path('', include('Api.urls')),

]
urlpatterns+=static(settings.MEDIA_URL,Document_root=settings.MEDIA_ROOT)
urlpatterns+=static(settings.STATIC_URL,Document_root=settings.STATIC_ROOT)