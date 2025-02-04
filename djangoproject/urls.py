from django.contrib import admin
from django.urls import path, include
from product import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home_app.urls')),
    path("__reload__/", include("django_browser_reload.urls")),
    path('action/', include('product.urls')),  
    path('user/', include('user_app.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
