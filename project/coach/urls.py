from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('coach/', views.coach, name='coach'),

]