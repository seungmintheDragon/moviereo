# Generated by Django 3.2.6 on 2022-11-18 04:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0007_auto_20221118_1321'),
    ]

    operations = [
        migrations.RenameField(
            model_name='moviecomment',
            old_name='Movie',
            new_name='movie',
        ),
        migrations.RemoveField(
            model_name='commentreply',
            name='reply',
        ),
        migrations.RemoveField(
            model_name='commentreply',
            name='replycomment',
        ),
        migrations.AddField(
            model_name='commentreply',
            name='moviecomment',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='replymoviecomment', to='movies.moviecomment'),
        ),
        migrations.AddField(
            model_name='commentreply',
            name='parent',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='reply', to='movies.commentreply'),
        ),
        migrations.AlterField(
            model_name='commentreply',
            name='comment',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]