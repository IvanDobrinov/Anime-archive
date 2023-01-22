from django.http import HttpResponse
from django.template import loader
from rest_framework.viewsets import ViewSet
from vsg.utils import get_base_context

from .models import Favorite
from .utils import query_jikan, add_is_favorite


def results_view(request, *args, **kwargs):
    user = request.user
    results = query_jikan(
        query=kwargs['query'], page=kwargs['page']
    )  # result format: {'pagination': {...}, 'data': [...]}
    if user.is_authenticated:
        results['data'] = add_is_favorite(results['data'])

    template = loader.get_template('results.html')
    context = {
        **get_base_context(request),
        **results,
        'title': 'Results for "{}"'.format(kwargs['query']),
        'query': kwargs['query'],
        'show_search': True,
    }
    return HttpResponse(
        template.render(context, request)
    )


def favorite_list(request, *args, **kwargs):
    user = request.user
    if not user.is_authenticated:
        return HttpResponse(status=401)

    results = Favorite.objects.for_user().values_list('result_data', flat=True)
    template = loader.get_template('results.html')
    context = {
        **get_base_context(request),
        'data': results,
        'title': 'Favorites',
    }
    return HttpResponse(
        template.render(context, request)
    )


class FavoriteView(ViewSet):
    def post(self, request, *args, **kwargs):
        user = request.user
        mal_id = request.data['mal_id']
        anime_data = query_jikan(mal_id=mal_id)

        Favorite.objects.create(user=user, mal_id=mal_id, result_data={**anime_data['data'], 'is_favorite': True})

        return HttpResponse(status=200)

    def delete(self, request, *args, **kwargs):
        mal_id = request.data['mal_id']
        Favorite.objects.for_user().filter(mal_id=mal_id).delete()
        return HttpResponse(status=200)
