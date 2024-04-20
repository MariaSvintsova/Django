from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls', namespace='main')),
    path('materials/', include('materials.urls', namespace='materials')),
    path('auth/', include('autentification.urls', namespace='auth'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
