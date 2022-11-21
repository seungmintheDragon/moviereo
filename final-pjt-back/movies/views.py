from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from django.db.models import Q


from .serializers import *
from .models import *
# Create your views here.

import random

@api_view(['GET', 'POST'])
def home_movies(request):
    if request.method == 'GET':
        movies = Movie.objects.all().order_by('?')[:4]

        serializer = HomeMovieSerializer(movies, many=True)
        return Response(serializer.data)
        

@api_view(['GET'])
def movie_detail(request, movie_pk):
    if request.method == 'GET':
        movie = get_object_or_404(Movie, pk=movie_pk)
        serializer = MovieDetailSerializer(movie)
        actor = movie.actor.all()
        genre = movie.genres.all()
        return Response(serializer.data)


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

@api_view(['GET','POST'])
def searchmovie(request, movie_title):
    if request.method == 'GET':
        data = {
            'title': movie_title,
        }
        # 쿼리 셋 유니온 기능 활용하기.
        # subject = Movie.objects.all().filter(title__contains=movie_title)
        subject = Movie.objects.all().filter(title__contains=movie_title)
        serializer = MovieDetailSerializer(subject, many=True)
        return Response(serializer.data)


@api_view(['GET'])
def likemovie(request):
    if request.method == 'GET':
        movie_list = LikeMovieList.objects.filter(user=request.user.id)
        serializer = LikeMovieListSerializer(movie_list, many=True)
        return Response(serializer.data)



@api_view(['POST'])
def likemovienew(request, movie_pk):
    if request.method == 'POST':
        movie = get_object_or_404(Movie, pk=movie_pk)
        serializer = LikeMovieListSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.user, movies=movie)
        return Response(serializer.data)

@api_view(['POST'])
def likemoviecreate(request, movie_pk, list_pk):
    if request.method == 'POST':
        movie = Movie.objects.get(pk=movie_pk)
        LikeMovieList.objects.get(pk=list_pk).movies.add(movie)
        serializer = LikeMovieListSerializer(movie)
        print(serializer.data)
        return Response(serializer.data)

        # except:
        #     movie = get_object_or_404(Movie, pk=movie_pk)
        #     serializer = LikeMovieListSerializer(data=request.data)
        #     if serializer.is_valid(raise_exception=True):
        #         serializer.save(user=request.user, movies=movie)
        #     return Response(serializer.data)

#코멘트 리스트
@api_view(['GET'])
def commentlist(request):
    if request.method == 'GET':
        comment = MovieComment.objects.all().filter(user=request.user)
        serializer = MovieCommentSerializer(comment, many=True)
        return Response(serializer.data)