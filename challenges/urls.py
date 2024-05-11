from . import views
from django.urls import path

urlpatterns = [
    path('', views.all_challenges, name='challenges'),
    path('add/', views.create_challenge, name='create_challenge'),
    path('<slug:slug>/', views.challenge_detail, name='challenge_detail'),    
]