from django.db import models

class Publication(models.Model):
    title=models.CharField(max_length=50)

    class meta:
        ordering = ["title"]

    def __str__(self):
        return self.title
    
class Article(models.Model):
    headline=models.CharField(max_length=100)
    publication=models.ManyToManyField(Publication)
    
    class meta:
        ordering=["headline"]

    def __str__(self):
        return self.headline