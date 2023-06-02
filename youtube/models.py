from django.db import models

# Create your models here.
class Writings(models.Model):
    id = models.BigAutoField(primary_key=True)
    content = models.TextField(default='')
    video_id = models.TextField(default='')