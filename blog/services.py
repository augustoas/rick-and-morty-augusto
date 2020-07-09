import requests

def generate_request(url, params={}):
    response = requests.get(url, params=params)

    if response.status_code == 200:
        return response.json()

def get_all_episodes(params={}): #CAMBIAR EL HOME INICIAL POR CONSULTA MÚLTIPLE.

    response = []
    for p in range(2):
        page = generate_request('https://rickandmortyapi.com/graphql?query={episodes(page:'+str(p+1)+'){results{name,id,air_date,episode}}}', params)
        response += page['data']['episodes']['results']

    if response:
        return response
    return ''

def get_episode_info(id,params={}):
   
    response = generate_request('https://rickandmortyapi.com/graphql?query={episode(id:'+str(id)+'){name,air_date,episode,characters{name, id}}}', params)
    response = response['data']['episode']
    if response:
        return response

    return ''

def search_character(query,params={}): #CAMBIAR EL HOME INICIAL POR CONSULTA MÚLTIPLE.
    response = []
    for p in range(30):
        url = 'https://rickandmortyapi.com/graphql?query={characters(page:'+str(p+1)+',filter:{name:"'+str(query)+'"}){results{name,id}}}'
        page = generate_request(url, params)
        if 'errors' in page.keys():
            continue
        else:
            response += page['data']['characters']['results']

    if response:
        return response

    return ''

def search_location(query,params={}): #CAMBIAR EL HOME INICIAL POR CONSULTA MÚLTIPLE.
    response = []
    for p in range(5):
        url = 'https://rickandmortyapi.com/graphql?query={locations(page:'+str(p+1)+',filter:{name:"'+str(query)+'"}){results{name,id}}}'
        page = generate_request(url, params)
        if 'errors' in page.keys():
            continue
        else:
            response += page['data']['locations']['results']

    if response:
        return response

    return ''

def search_episode(query,params={}): #CAMBIAR EL HOME INICIAL POR CONSULTA MÚLTIPLE.
    response = []
    for p in range(2):
        url = 'https://rickandmortyapi.com/graphql?query={episodes(page:'+str(p+1)+',filter:{name:"'+str(query)+'"}){results{name,id, episode}}}'
        page = generate_request(url, params)
        if 'errors' in page.keys():
            continue
        else:
            response += page['data']['episodes']['results']

    if response:
        return response

    return ''

def get_character(id,params={}):

    response = generate_request('https://rickandmortyapi.com/graphql?query={character(id:'+str(id)+'){name,status,species,image,location{name,id},origin{name,id},episode{name, id}}}', params)
    response = response['data']['character']

    if response:
        return response

    return ''

def get_place(id, params={}):
    
    response = generate_request('https://rickandmortyapi.com/graphql?query={location(id:'+str(id)+'){name,id,type,dimension,residents{name,id}}}', params)
    response = response['data']['location']

    if response:
        return response

    return ''

