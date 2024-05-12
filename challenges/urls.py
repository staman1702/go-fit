from . import views
from django.urls import path

urlpatterns = [
    path('', views.all_challenges, name='challenges'),
    path('add/', views.create_challenge, name='create_challenge'),
    path('edit/<slug:slug>/', views.edit_challenge, name='edit_challenge'),
    path('delete/<slug:slug>/', views.delete_challenge, name='delete_challenge'),
    path('<slug:slug>/', views.challenge_detail, name='challenge_detail'),    
]