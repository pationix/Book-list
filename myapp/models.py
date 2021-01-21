from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=50, null=True, blank=True)
    readed = models.DateField(default=None, null=True, blank=True)
    review = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['title']