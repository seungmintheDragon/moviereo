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
        
