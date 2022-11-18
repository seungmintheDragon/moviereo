from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

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
        print(actor)
        print(genre)
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

            if serializer.is_valid(raise_exception=True):
                serializer.save(user=request.user, movie=movie_pk)
                return Response(serializer.data)


@api_view(['GET','POST'])
def replycomment(request, movie_pk, comment_pk):
    if request.method =='GET':
        reply = CommentReply.objects.filter()
        pass