# Generated by Django 3.2.6 on 2022-11-18 06:08

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0008_auto_20221118_1335'),
    ]

    operations = [
        migrations.AddField(
            model_name='moviecomment',
            name='rate',
            field=models.IntegerField(default=1, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(10)]),
            preserve_default=False,
        ),
    ]