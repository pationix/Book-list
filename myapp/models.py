from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=50)
    readed = models.DateTimeField('date readed')
    review = models.CharField(max_length=200)