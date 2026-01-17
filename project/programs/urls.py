from django.urls import path
from . import views

urlpatterns = [
    # Страницы программ и категорий
    path('program/', views.program, name='program'),
    path('program/<int:category_id>/', views.program, name='category'),

    # Страница тренировки
    path('programs/<int:pk>/', views.workouts, name='workouts'),

    # Регистрация
    path('register/', views.register, name='register'),

    # Действия с избранным (добавлены префиксы!)
    path('programs/<int:exercise_id>/add-to-favourites/',
         views.add_to_favourites, name='add_to_favourites'),
    path('programs/<int:exercise_id>/remove-from-favourites/',
         views.remove_from_favourites, name='remove_from_favourites'),
]