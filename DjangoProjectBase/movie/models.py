from django.db import models

# create your models here

class Movie(models.Model): 
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=250) 
    image = models.ImageField(upload_to='movie/images/', default = 'movie/images/default.jpg') 
    url = models.URLField(blank=True)
    genre = models.CharField(blank=True, max_length=250)
    year = models.IntegerField(blank=True, null=True)

    def __str__(self): 
        return self.title
