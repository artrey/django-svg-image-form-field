from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/articles')
    text = models.TextField()
