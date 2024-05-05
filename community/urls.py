from . import views
from django.urls import path

urlpatterns = [
    path('', views.all_posts, name='community'),
    path('add/', views.add_post, name='add_post'),
    path('edit/<slug:slug>/', views.edit_post, name='edit_post'),
    path('<slug:slug>/', views.post_detail, name='post_detail'),    
]
