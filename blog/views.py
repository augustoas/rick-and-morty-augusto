# Create your views here. las views en django son como los controlers en MVC.
from django.shortcuts import render
import requests
from .services import get_all_episodes, get_episode_info, get_character, get_place, search_character, search_episode, search_location

def home(request):

    context = {
                'episodes': get_all_episodes
            }
    return render(request, 'blog/home.html', context) #Enviando context acá da acceso a posts desde el template. 


def episode_info(request, id):
    
    episode = get_episode_info(id)
    context = {
            'episode': episode,
            'characters': episode['characters']
        }
    return render(request, 'blog/episode_info.html',context)


def character_info(request, id):

    character = get_character(id)
    context = {
            'character': character,
            'episodes_char': character['episode'],
            'char_location': character['location'],
            'char_origin': character['origin']
        }
    return render(request, 'blog/character_info.html',context)

def place_info(request, id):

    place = get_place(id)
    context = {
            'place': place,
            'residents':place['residents']
        }

    return render(request, 'blog/place_info.html',context)

def search_info(request):

    query = request.GET.get('query')
    characters = search_character(query)
    episodes = search_episode(query)
    locations = search_location(query)

    context = {
            'characters': characters,
            'episodes':episodes,
            'locations':locations,
            'query':query
        }

    return render(request, 'blog/search_info.html',context)
