import json

import requests

from .models import Favorite

LIST_REQUEST_TEMPLATE = 'https://api.jikan.moe/v4/anime?q={query}&sfw'
SINGLE_REQUEST_TEMPLATE = 'https://api.jikan.moe/v4/anime/{}'


def query_jikan(mal_id=None, query=None, page=None):
    if not mal_id:
        url = LIST_REQUEST_TEMPLATE.format(query=query)
        if page:
            url += f'&page={page}'
    else:
        url = SINGLE_REQUEST_TEMPLATE.format(mal_id)

    response = requests.get(url)
    data = json.loads(response.content)

    return data


def add_is_favorite(animes):
    if not isinstance(animes, list):
        animes = [animes]
    favorites = Favorite.objects.for_user().values_list('mal_id', flat=True)
    for anime in animes:
        if anime['mal_id'] in favorites:
            anime['is_favorite'] = True
    return animes
