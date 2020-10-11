from django.urls import path
from .views import (
    game_view,
    player_create_view,
    start_page_view,
    game_create_view,
)

app_name = 'game'
urlpatterns = [
    path('', start_page_view, name='start-page'),
    path('settings/', game_create_view, name='game-create'),
    path('game/', game_view, name='game'),
    path('player/', player_create_view, name='player-create'),
]
