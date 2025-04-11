from django.urls import path
from . import views

urlpatterns = [
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('posts/', views.post_list, name='post_list'),  # ✅ 목록 추가
    path('write/', views.post_create, name='post_create'),
    path('graph/', views.graph_view, name='graph_view'),
    path('graph/data/', views.graph_data, name='graph_data'),
]

