from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),  # ✅ 이 줄 꼭 있어야 blog.urls 연결됨!
]
