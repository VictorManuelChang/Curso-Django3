from django.contrib import admin
from django.urls import path, include
from .views import hello_world
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', hello_world),
    path('blog/', include('website.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)