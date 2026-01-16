from django.urls import path
from . import views

urlpatterns = [
    path('program/', views.program, name='program'),
    path('program/<int:category_id>/', views.program, name='category'),
    path('programs/<int:pk>/', views.workouts, name='workouts'),


]