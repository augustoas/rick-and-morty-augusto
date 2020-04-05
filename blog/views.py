# Create your views here. las views en django son como los controlers en MVC.
from django.shortcuts import render
import requests
from .services import get_all_episodes, get_episode_info, get_characters, get_character, get_episodes, get_place, get_places, get_all_places, get_all_characters

def home(request):

    context = {
                'episodes': get_all_episodes
            }
    return render(request, 'blog/home.html', context) #Enviando context acá da acceso a posts desde el template. 


def episode_info(request, id):
    
    id_list = []
    episode = get_episode_info(id)
    for char in episode['characters']:
        id_list.append(int(char.split('/')[-1]))

    context = {
            'episode': episode,
            'characters': get_characters(id_list)
        }
    return render(request, 'blog/episode_info.html',context)


def character_info(request, id):

    id_ep_list = []
    character = get_character(id)
    for ep in character['episode']:
        id_ep_list.append(int(ep.split('/')[-1]))



    context = {
            'character': character,
            'episodes_char': get_episodes(id_ep_list),
            'char_location_id': character['location']['url'].split('/')[-1],
            'char_origin_id': character['origin']['url'].split('/')[-1]
        }
    return render(request, 'blog/character_info.html',context)

def place_info(request, id):

    id_char_list = []
    place = get_place(id)

    

    for char in place['residents']:
        id_char_list.append(int(char.split('/')[-1]))
    context = {
            'place': place,
            'residents':get_characters(id_char_list)
        }

    return render(request, 'blog/place_info.html',context)

def search_info(request):

    query = request.GET.get('query')

    episodes = get_all_episodes()
    characters = get_all_characters()
    places = get_all_places()

    filter_episodes = [e for e in episodes if query in e['name'].lower()]
    filter_characters = [c for c in characters if query in c['name'].lower()]
    filter_places = [p for p in places if query in p['name'].lower()]
    
    

    context = {
            'episodes': filter_episodes,
            'characters': filter_characters,
            'places': filter_places,
            'query':query
        }

    return render(request, 'blog/search_info.html',context)
