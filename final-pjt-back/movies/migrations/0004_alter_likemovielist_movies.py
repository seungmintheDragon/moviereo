# Generated by Django 3.2.6 on 2022-11-22 08:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0003_alter_likemovielist_movies'),
    ]

    operations = [
        migrations.AlterField(
            model_name='likemovielist',
            name='movies',
            field=models.ManyToManyField(blank=True, related_name='user_like_movie_list', to='movies.Movie'),
        ),
    ]
