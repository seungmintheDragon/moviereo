from django.urls import path
from . import views


urlpatterns = [
    path('', views.home_movies),
    path('<int:movie_pk>/', views.movie_detail),
    path('<int:movie_pk>/comment/', views.movie_comment),
    path('<int:movie_pk>/comment/<int:comment_pk>/', views.replycomment),
]