from django.urls import path, include

from . import views

urlpatterns = [
    path('<str:query>/<int:page>', views.results_view, name='results'),
    path('favorites', views.favorite_list, name='favorites'),
    path('favorite', views.FavoriteView.as_view({'post': 'post'}), name='favorite'),
    path('favorite', views.FavoriteView.as_view({'delete': 'delete'}), name='unfavorite'),
]
