from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('accounts/', include('auth_app.urls')),
    path('profile/', include('profil.urls')),
    path('comment/', include('comment.urls')),


    path('tinymce/',include('tinymce.urls')),
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
