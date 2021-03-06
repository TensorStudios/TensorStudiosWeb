from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('postlist/', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('about/', views.about, name='about'),
    path('projectlist/', views.project_list, name='project_list'),
    path('project/<int:pk>/', views.project_detail, name='project_detail'),
]
