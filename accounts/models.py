from django.db import models
from django.contrib.auth.models import User
from home.views import Anime


class UserProfile(models.Model):
    hobbies = models.CharField(max_length = 200, null=True)
    image = models.URLField(null = True)
    address = models.CharField(max_length = 100, null = True)
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    watchList = models.ManyToManyField(Anime, blank = True)

    def __str__(self) -> str:
        return self.user.username



