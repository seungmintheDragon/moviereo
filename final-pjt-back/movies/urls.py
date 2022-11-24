from django.urls import path
from . import views


urlpatterns = [
    path('nothing/', views.nothing),
    path('', views.home_movies),
    path('<int:movie_pk>/', views.movie_detail),
    path('<int:movie_pk>/comment/', views.movie_comment),
    path('<int:movie_pk>/comment/<int:comment_pk>/', views.movie_comment_dp),
    # path('<int:movie_pk>/comment/<int:comment_pk>/', views.replycomment),
    path('search/<str:movie_title>/', views.searchmovie),
    # 추천 페이지
    path('recommend/', views.recommend),
    # 영화 리스트
    path('likemovie/', views.likemovie),
    path('likemovienew/', views.likemovienew),
    path('likemovielist/<int:movie_pk>/append/<int:list_pk>/', views.likemoviecreate),

    # 코멘트 리스트
    path('comment/', views.commentlist),

    # 장르별
    path('genre/<int:genre_pk>/', views.genre_movie),

    # 배우별
    path('actor/<int:actor_pk>/', views.actor_movie),
    # 감독별
    path('director/<int:director_pk>/', views.director_movie),

    # 인기순
    path('popular/', views.popular),

    # 온스크린
    path('onscreen/', views.onscreen),

    path('nothing/', views.nothing),
]