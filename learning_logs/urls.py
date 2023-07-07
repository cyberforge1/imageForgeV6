"""Defines URL patterns for learning_logs."""

from django.urls import path

from . import views
from .views import execute_prompt_file, execute_image_file

app_name = 'learning_logs'
urlpatterns = [
    # Home page
    path('', views.index, name='index'),
    # Page that shows all topics.
    path('generation/', views.generation, name='generation'),
    # Page that displays the generated images
    path('gallery/', views.gallery, name='gallery'),
    # Page that displays the user image generation history
    path('user_history/', views.user_history, name='user_history'),
    # Page to show the about us content
    path('about/', views.about, name='about'),
    
    
    #Button Click Executions
    # Prompt Execution URL
    path('execute_prompt_file/', execute_prompt_file, name='execute_prompt_file'),
    # Image Execution URL
    path('execute_image_file/', execute_image_file, name='execute_image_file'),
    
]