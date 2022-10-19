import os
import django
import requests


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "tvt.settings")

django.setup()

from home.models import Anime, Genre

for i in range(0, 2000):
    response = requests.get(f'https://api.jikan.moe/v4/anime/{i}')
    anime_inst = Anime() 

    try:
        data = response.json()['data']

        title = data['title']
        anime_inst.title = title

        img = data['images']['jpg']['image_url']
        anime_inst.img = img

        synopsis = data['synopsis']
        anime_inst.synopsis = synopsis

        num_of_episodes = data['episodes']
        anime_inst.num_of_episode = num_of_episodes

        anime_inst.save()

        for g in data['genres']:
            genre, created = Genre.objects.get_or_create(name = g['name'])
            genre.animes.add(anime_inst)
    
    except:
        continue