import requests

def generate_request(url, params={}):
    response = requests.get(url, params=params)

    if response.status_code == 200:
        return response.json()

def get_all_episodes(params={}): #CAMBIAR EL HOME INICIAL POR CONSULTA MÚLTIPLE.
    res = generate_request('https://rickandmortyapi.com/api/episode', params)
    total_ep_list = [x+1 for x in range(int(res['info']['count']))] 
    response = generate_request(f'https://rickandmortyapi.com/api/episode/{total_ep_list}', params)
    if response:
        return response

    return ''

def get_episodes(list_id, params={}):
    response = generate_request(f'https://rickandmortyapi.com/api/episode/{list_id}', params)
    if response:
        return response

    return ''

def get_episode_info(id,params={}):
    response = generate_request(f'https://rickandmortyapi.com/api/episode/{id}', params)

    if response:
        return response

    return ''

def get_all_characters(params={}): #CAMBIAR EL HOME INICIAL POR CONSULTA MÚLTIPLE.
    res = generate_request('https://rickandmortyapi.com/api/character', params)
    total_char_list = [x+1 for x in range(int(res['info']['count']))] 
    response = generate_request(f'https://rickandmortyapi.com/api/character/{total_char_list}', params)
    if response:
        return response

    return ''

def get_characters(list_id,params={}):

    response = generate_request(f'https://rickandmortyapi.com/api/character/{list_id}', params)

    if response:
        return response

    return ''

def get_character(id,params={}):

    response = generate_request(f'https://rickandmortyapi.com/api/character/{id}', params)

    if response:
        return response

    return ''

def get_all_places(params={}): #CAMBIAR EL HOME INICIAL POR CONSULTA MÚLTIPLE.
    res = generate_request('https://rickandmortyapi.com/api/location', params)
    total_pl_list = [x+1 for x in range(int(res['info']['count']))] 
    response = generate_request(f'https://rickandmortyapi.com/api/location/{total_pl_list}', params)
    if response:
        return response

    return ''

def get_place(id, params={}):
    response = generate_request(f'https://rickandmortyapi.com/api/location/{id}', params)
    if response:
        return response

    return ''

def get_places(list_id, params={}):
    response = generate_request(f'https://rickandmortyapi.com/api/location/{list_id}', params)
    if response:
        return response['results']

    return ''


total_ep_list = [x+1 for x in range(10)]
print(total_ep_list)