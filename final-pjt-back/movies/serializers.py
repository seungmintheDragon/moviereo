from rest_framework import serializers
from .models import *
# from accounts.serializers import UserSerializer


class HomeMovieSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = "__all__"


class ActorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Actor
        fields = "__all__"


class GenreSerializer(serializers.ModelSerializer):

    class Meta:
        model = Genre
        fields = "__all__"

class DirectorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Director
        fields = "__all__"




class MovieDetailSerializer(serializers.ModelSerializer):
    genres = GenreSerializer(many=True)
    actor = ActorSerializer(many=True)
    director = DirectorSerializer(many=True)

    class Meta:
        model = Movie
        fields = "__all__"