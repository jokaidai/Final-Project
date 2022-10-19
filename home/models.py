from django.db import models
from django.urls import reverse


class Genre(models.Model):
    name = models.CharField(max_length = 50)
    img = models.URLField(blank = True, null = True)

    def __str__(self) -> str:
        return self.name

    def get_absolute_url(self):
        return reverse('animes_list', args = [self.id])

class Anime(models.Model):

    class Meta : 
        ordering = ['-like']

    title = models.CharField(max_length = 50, blank = True, null = True)
    img = models.URLField(blank = True, null = True)
    genres = models.ManyToManyField(Genre, related_name = 'animes')
    synopsis = models.TextField(max_length = 2000, blank = True, null = True)
    num_of_episode = models.IntegerField(blank = True, null = True)
    like = models.IntegerField(default = 0)
    dislike = models.IntegerField(default = 0)

    def __str__(self) -> str:
        return self.title

    def get_absolute_url(self):
        return reverse('about_anime', args = [self.id])