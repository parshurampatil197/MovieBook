from django.urls import path
from .views import *

urlpatterns = {
    path('', index_view),
    path('listmovies/', list_movies_view),
    path('addmovie/', add_movie_view),
}