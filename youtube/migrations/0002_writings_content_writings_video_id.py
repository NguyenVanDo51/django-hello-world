# Generated by Django 4.1.9 on 2023-06-02 10:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('youtube', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='writings',
            name='content',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='writings',
            name='video_id',
            field=models.TextField(default=''),
        ),
    ]
