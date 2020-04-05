from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name= 'blog-home'),
    path('episode_info/<int:id>/', views.episode_info, name= 'blog-episode_info'),
    path('character_info/<int:id>/', views.character_info, name= 'blog-character_info'),
    path('place_info/<int:id>/', views.place_info, name= 'blog-place_info'),
    path('search_info', views.search_info, name= 'blog-search_info'),
]
