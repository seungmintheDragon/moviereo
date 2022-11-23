from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from django.db.models import Q
from . import recommande_movie
# from . import movieitem

from .serializers import *
from .models import *
# Create your views here.


@api_view(['GET', 'POST'])
def home_movies(request):
    if request.method == 'GET':
        movies = Movie.objects.all().order_by('?')[:4]

        serializer = HomeMovieSerializer(movies, many=True)
        return Response(serializer.data)
        

@api_view(['GET'])
def movie_detail(request, movie_pk):
    if request.method == 'GET':
        try:
            movie = Movie.objects.get(pk=movie_pk)
            serializer = MovieDetailSerializer(movie)
            return Response(serializer.data)
        except:

            return Response(status=status.HTTP_403_FORBIDDEN)


@api_view(['GET','POST'])
def movie_comment(request, movie_pk):
    if request.method =='GET':
        comment = MovieComment.objects.filter(movie=movie_pk)
        serializer = MovieCommentSerializer(comment, many=True)

        return Response(serializer.data)

    elif request.method == 'POST':
        if request.user.is_authenticated:
            serializer = MovieCommentSerializer(data=request.data)
            moviec = get_object_or_404(Movie, pk=movie_pk)
            if serializer.is_valid(raise_exception=True):
                serializer.save(user=request.user, movie=moviec)
                return Response(serializer.data)

@api_view(['PUT','DELETE'])
@permission_classes([IsAuthenticated])
def movie_comment_dp(request, movie_pk, comment_pk):
    comment = MovieComment.objects.get(pk=comment_pk)
    if request.method == 'DELETE':
        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    elif request.method == 'PUT':
        serializer = MovieCommentSerializer(comment, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
        


@api_view(['GET','POST'])
def searchmovie(request, movie_title):
    if request.method == 'GET':
        data = {
            'title': movie_title,
        }
        # 쿼리 셋 유니온 기능 활용하기.
        subject = Movie.objects.all().filter(title__contains=movie_title)
        serializer = MovieDetailSerializer(subject, many=True)
        return Response(serializer.data)

    # elif mode in ('release_date', 'vote_average', 'popularity'):
    #     if mode != 'vote_average':
    #         movies = Movie.objects.order_by(f'-{mode}')[:100]
    #     else:
    #         movies = Movie.objects.annotate(vote_average=(F('tmdb_vote_sum') + F('our_vote_sum')) / (F('tmdb_vote_cnt') + F('our_vote_cnt'))).order_by('-vote_average')[:100]
    # elif mode in ('director', 'actor', 'title'):
    # # 조회 2. mode - 감독별, 배우별, 영화명별
    #     inputValue = request.GET.get('inputValue')
    #     if mode == 'director':
    #         # MtoM 관계에서 원하는 조건을 가지는 영화들을 가져오는 방법
    #         # https://docs.djangoproject.com/en/3.2/topics/db/examples/many_to_many/
    #         movies = Movie.objects.filter(Q(directors__name__icontains=inputValue)|Q(directors__original_name__icontains=inputValue)).distinct()[:100]
    #     elif mode == 'actor':
    #         movies = Movie.objects.filter(Q(actors__name__icontains=inputValue)|Q(actors__original_name__icontains=inputValue)).distinct()[:100]
    #     else:
    #         # 한글 제목이나 원본 제목이 사용자의 입력(inputValue)를 포함하는 영화들을 반환(대소문자 구분하지 않음)
    #         movies = Movie.objects.filter(Q(title__icontains=inputValue)|Q(original_title__icontains=inputValue))[:100]
    # # 조회 3. mode - 장르별
    # elif mode == 'genre':
    #     inputGenre = request.GET.get('inputGenre')
    #     movies = Movie.objects.filter(genres__tmdb_genre_id=inputGenre)[:100]

    # serializer = MovieListSerializer(movies, many=True)
    # return Response(serializer.data)


@api_view(['GET'])
def likemovie(request):
    if request.method == 'GET':
        movie_list = LikeMovieList.objects.filter(user=request.user.id)
        serializer = LikeMovieListSerializer(movie_list, many=True)
        return Response(serializer.data)

@api_view(['POST'])
def likemovienew(request):
    if request.method == 'POST':
        serializer = LikeMovieListSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.user)
        return Response(serializer.data)

@api_view(['POST', 'PUT', 'DELETE'])
def likemoviecreate(request, movie_pk, list_pk):
    movie = Movie.objects.get(pk=movie_pk)
    if request.method == 'POST':
        LikeMovieList.objects.get(pk=list_pk).movies.add(movie)
        serializer = LikeMovieListSerializer(movie)
        return Response(serializer.data)
    elif request.method == 'PUT':
        LikeMovieList.objects.get(pk=list_pk).movies.remove(movie)
        serializer = LikeMovieListSerializer(movie)
        return Response(serializer.data)
    elif request.method == 'DELETE':
        likemovielist = LikeMovieList.objects.get(pk=list_pk)
        likemovielist.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)




#코멘트 리스트
@api_view(['GET'])
def commentlist(request):
    if request.method == 'GET':
        comment = MovieComment.objects.all().filter(user=request.user)
        serializer = MovieCommentSerializer(comment, many=True)
        return Response(serializer.data)




@api_view(['POST'])
def recommend(request):
    if request.method =='POST':
        movies_id = recommande_movie.resforreco(request.data['movies'])
        movies = Movie.objects.filter(id__in=movies_id)
        serializer = MovieDetailSerializer(movies, many=True)
        if len(serializer.data) == 0:
            return Response(status=status.HTTP_406_NOT_ACCEPTABLE)
        return Response(serializer.data)