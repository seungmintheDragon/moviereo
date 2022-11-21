from django.urls import path
from . import views


urlpatterns = [
    path('', views.home_movies),
    path('<int:movie_pk>/', views.movie_detail),
    path('<int:movie_pk>/comment/', views.movie_comment),
    # path('<int:movie_pk>/comment/<int:comment_pk>/', views.replycomment),
    path('search/<str:movie_title>/', views.searchmovie),
    # 추천 페이지
    # 
    # 영화 리스트
    path('likemovie/', views.likemovie),
    path('likemovienew/', views.likemovienew),
    path('likemovielist/<int:movie_pk>/<int:list_pk>/', views.likemoviecreate),

    # 코멘트 리스트
    path('comment/', views.commentlist),
]