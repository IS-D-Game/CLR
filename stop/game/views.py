from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .forms import AnswerForm
from .forms import PlayerForm
from .models import Player
from .models import Answer
from .models import Settings


# Create your views here.
def game_view(request, game_id, player_name):
    obj = Settings.objects.get(game_id=game_id)
    obj2 = Player.objects.get(player_name=player_name)
    form = AnswerForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
    context = {
        "form" : form,
    }
    return render(request, "game/game.html", context)


def player_create_view(request):
    form = PlayerForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = PlayerForm()
    context = {
        'form': form
    }
    return render(request, "game/player_create.html", context)


def start_page_view(request):
    return render(request, "game/start_page.html")

def game_create_view(request):
    return render(request, "game/game_create.html")


