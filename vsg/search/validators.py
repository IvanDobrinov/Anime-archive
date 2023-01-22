from django.core.exceptions import ValidationError
from threadlocals.threadlocals import get_current_request


def unique_for_user(value):
    from vsg.search.models import Favorite
    request = get_current_request()
    if Favorite.objects.filter(user=request.user, mal_id=value).exists():
        raise ValidationError('Title is already favorited!')