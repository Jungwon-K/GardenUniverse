from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='home'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('posts/', views.post_list, name='post_list'),  # ✅ 목록 추가
    path('write/', views.post_create, name='post_create'),
    path('graph/', views.graph_view, name='graph_view'),
    path('graph/data/', views.graph_data, name='graph_data'),
    path('login/', auth_views.LoginView.as_view(template_name='blog/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]

