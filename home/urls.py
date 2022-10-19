from django.urls import path
from .views import (
    home,
    search_error,
    genres_view,
    anime_view,
    anime_about_view,
    anime_search_view,
    WIP
)

urlpatterns = [
path('', home, name = 'home'),
path('support/search_error', search_error, name = 'search_error'),
path('support/WIP', WIP, name = 'WIP'),
path('genres_list', genres_view, name = 'genres_list'),
path('anime_list/<int:id>', anime_view, name = 'animes_list'),
path('about_anime/<int:id>', anime_about_view, name = 'about_anime'),
path('anime_search', anime_search_view, name = 'anime_search')
]