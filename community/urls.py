from . import views
from django.urls import path

urlpatterns = [
    path('', views.all_posts, name='community'),
    path('add/', views.add_post, name='add_post'),
    path('edit_comment/<int:comment_id>/', views.edit_comment, name='edit_comment'),
    path('delete_comment/<int:comment_id>/', views.delete_comment, name='delete_comment'),
    path('edit/<slug:slug>/', views.edit_post, name='edit_post'),
    path('delete/<slug:slug>/', views.delete_post, name='delete_post'),    
    path('<slug:slug>/', views.post_detail, name='post_detail'),    
]
