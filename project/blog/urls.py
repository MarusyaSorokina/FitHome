from django.urls import path
from . import views


urlpatterns = [
    path('', views.blog_list, name="post_list"),
    path('<int:post_id>/', views.detail, name="detail"),
]