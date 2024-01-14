from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from cinema.views import (MovieViewSet,
                          GenreViewSet,
                          ActorViewSet, CinemaHallViewSet)

router = routers.DefaultRouter()
router.register("movies", MovieViewSet)
router.register("genres", GenreViewSet)
router.register("actors", ActorViewSet)
router.register("cinema_halls", CinemaHallViewSet)


urlpatterns = [
    path("", include(router.urls)),
]

app_name = "cinema"
