from django.urls import path
from .views import (
    game_view,
    player_create_view,
    player_create_view_2,
    start_page_view,
    game_create_view,
    evaluation_view,
    leaderboard_view,
)

app_name = 'game'

urlpatterns = [
    path('', start_page_view, name='start-page'),
    path('settings/', game_create_view, name='game-create'),
    path('game/<str:player_name>/<int:game_id>/', game_view, name='game'),
    path('player/', player_create_view, name='player-create'),
    path('player/<int:game_id>/', player_create_view_2, name='player-create_2'),
    path('evaluation/<str:player_name>/<int:game_id>/', evaluation_view, name='evaluation-create'),
    path('leaderboard/<str:player_name>/<int:game_id>/', leaderboard_view, name='leaderboard-page')
]
