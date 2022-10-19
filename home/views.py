from django.shortcuts import render, redirect
import random
from .models import Genre, Anime

def home(request):
    welcome_message = "Welcome to Tv Tracker the best place to find shows and movie to watch and track your progression watching them !!!"
    return render(request, 'homepage.html', {'message': welcome_message})

def search_error(request):
    error_message = "Oops didn't find what you where looking for ...."
    return render(request, 'support/search_error.html', {'message': error_message})

def WIP(request):
    announcement = 'Work in Progress comme Back Later !!'
    return render(request, 'support/WIP.html', {'message': announcement})

def genres_view(request):
    genres = Genre.objects.all()
    for genre in genres:
        anim_list = genre.animes.all()
        rand_img = random.choice(anim_list)
        genre.img = rand_img.img
        genre.save()
    
    return render(request, 'genres_list.html', {'genres': genres})

def anime_view(request, id):

    genre = Genre.objects.get(id = id)
    animes = genre.animes.all()
    context = {"animes_list" : animes, "genre":genre}

    return render(request, "animes_list.html", context)

def anime_about_view(request, id):
    anime = Anime.objects.get(id = id)
    return render(request, "anime_about.html", {'anime': anime})


def anime_search_view(request):
    query_dict = request.GET
    try:
        query = query_dict.get('search')
    except:
        query = None
    if query is not None:
        anime = Anime.objects.filter(title__icontains = query).first()
        if not anime:
            return redirect('search_error') 

        return redirect('about_anime', id = anime.id)
    else:
        return redirect('search_error') 
    