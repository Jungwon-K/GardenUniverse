from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),  # ✅ 이 줄 꼭 있어야 blog.urls 연결됨!
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
