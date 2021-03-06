# Generated by Django 3.2 on 2021-08-06 15:06

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_auto_20210805_2204'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='dislikes',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='video',
            name='thumbnail',
            field=models.ImageField(default=None, upload_to=''),
        ),
        migrations.AddField(
            model_name='video',
            name='video',
            field=models.FileField(default=None, upload_to='videos_uploaded', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['MOV', 'avi', 'mp4', 'webm', 'mkv'])]),
        ),
    ]
