from django.conf import settings
from django.db import models

from .managers import FavoriteManager
from .validators import unique_for_user


# Create your models here.


class Favorite(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    mal_id = models.IntegerField(validators=[unique_for_user])
    result_data = models.JSONField(default=dict)

    objects = FavoriteManager()
