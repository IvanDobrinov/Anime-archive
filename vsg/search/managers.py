from django.db import models
from threadlocals.threadlocals import get_current_request


class FavoriteManager(models.Manager):
    def for_user(self, user=None):
        if not user:
            user = get_current_request().user
        return self.filter(user=user)
