from rest_framework import serializers
from .models import *
from accounts.serializers import UserSerializer


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



# 코멘트에 등록할 무비 시리얼라이즈
class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ('id','title',)

# 코멘트 리플라이
class ReflyCommentSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    reply = serializers.SerializerMethodField()

    class Meta:
        model = CommentReply
        fields = "__all__"


# 코멘트 시리얼 라이즈
class MovieCommentSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    movie = MovieSerializer(read_only=True)
    replymoviecomment = ReflyCommentSerializer(many=True, read_only=True)

    class Meta:
        model = MovieComment
        fields = "__all__"

class MovieCommentSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    movie = MovieSerializer(read_only=True)
    replymoviecomment = ReflyCommentSerializer(many=True, read_only=True)

    class Meta:
        model = MovieComment
        fields = "__all__"


class ReMovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Relatemovie
        fields = "__all__"





# 영화 상세정보
class MovieDetailSerializer(serializers.ModelSerializer):
    genres = GenreSerializer(many=True)
    actor = ActorSerializer(many=True)
    director = DirectorSerializer(many=True)
    comment = MovieCommentSerializer(many=True)
    relate_movie = ReMovieSerializer(many=True)

    class Meta:
        model = Movie
        fields = "__all__"

class MovieforLike(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ('title', 'id')
    


class LikeMovieListSerializer(serializers.ModelSerializer):
    movies =  MovieDetailSerializer(many=True, read_only=True)
    user = UserSerializer(read_only=True)

    class Meta:
        model = LikeMovieList
        fields = "__all__"