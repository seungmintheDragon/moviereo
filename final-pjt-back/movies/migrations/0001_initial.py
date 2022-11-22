# Generated by Django 3.2.6 on 2022-11-21 23:50

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Actor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('profile_path', models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Director',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('profile_path', models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('release_date', models.DateField()),
                ('popularity', models.FloatField()),
                ('vote_count', models.IntegerField()),
                ('vote_average', models.FloatField()),
                ('overview', models.TextField()),
                ('poster_path', models.CharField(max_length=200)),
                ('backdrop_path', models.CharField(max_length=200, null=True)),
                ('actor', models.ManyToManyField(to='movies.Actor')),
                ('director', models.ManyToManyField(to='movies.Director')),
                ('genres', models.ManyToManyField(to='movies.Genre')),
            ],
        ),
        migrations.CreateModel(
            name='Relatemovie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('poster_path', models.CharField(max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='MovieComment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField()),
                ('rate', models.FloatField(validators=[django.core.validators.MinValueValidator(0.5), django.core.validators.MaxValueValidator(5)])),
                ('movie', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comment', to='movies.movie')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='movie',
            name='relate_movie',
            field=models.ManyToManyField(to='movies.Relatemovie'),
        ),
        migrations.CreateModel(
            name='LikeMovieList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('movies', models.ManyToManyField(related_name='user_like_movie_list', to='movies.Movie')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_like_movie', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='CommentReply',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField()),
                ('moviecomment', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='replymoviecomment', to='movies.moviecomment')),
                ('parent', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='reply', to='movies.commentreply')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reply_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
