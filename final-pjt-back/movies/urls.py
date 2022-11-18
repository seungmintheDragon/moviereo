from django.urls import path
from . import views


urlpatterns = [
    path('', views.home_movies),
    path('<int:movie_pk>/', views.movie_detail),
    # path('<int:todo_pk>/', views.todo_update_delete),
]