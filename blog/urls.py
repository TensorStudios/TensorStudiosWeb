from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('postlist/', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
#    path('blog/login/', views.user_login, name='user_login'),
]
