from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
import json
from .forms import AnswerForm
from .forms import PlayerForm
from .forms import EvaluationForm
from .models import Player
from .models import Answer
from .models import Settings
from .models import Evaluation


# Create your views here.
def game_view(request, game_id, player_name):
    if request.method == "GET":
        # obj = Settings.objects.get(game_id=game_id)
        obj2 = Player.objects.get(player_name=player_name)
        # obj3 = Player.objects.get(game_id=game_id)
        form = AnswerForm(request.POST or None, instance=obj2)
        context = {
            "form" : form,
         }
        return render(request, "game/game.html", context)
    elif request.method == "POST":
        form = AnswerForm(request.POST or None)
        if form.is_valid():
            form.save()
        return redirect('/evaluation') #zu auswertung




def player_create_view(request):
    if request.method == "GET":
        form = PlayerForm()
        context = {
            'form': form
        }
        return render(request, "game/player_create.html", context)
    elif request.method == "POST":
        form = PlayerForm(request.POST or None)
        form.save()
        # if form.is_valid():
        context = {
            'form': form,
        }

        return redirect('/game/'+form.data['player_name']+'/'+form.data['game_id'], context)
        # else:
        #     context = {
        #         'error': "Error occures"
        #     }
        #     return render(request, "game/player_create.html", context)





def start_page_view(request):
    return render(request, "game/start_page.html")

def game_create_view(request):
    return render(request, "game/game_create.html")



def evaluation_view(request):
    if request.method == "GET":
        queryset_category = (Settings.objects.filter(game_id=123456).values('category_1', 'category_2', 'category_3', 'category_4',
                                                                 'category_5'))
        queryset = (Answer.objects.filter(game_id=123456).values('player_name', 'answer_1', 'answer_2', 'answer_3',
                                                           'answer_4', 'answer_5'))
        form = EvaluationForm(request.POST or None)
        context = {
            "form" : form,
            "answer_list" : queryset,
            "category_list" : queryset_category
         }
        return render(request, "game/evaluation.html", context)
    elif request.method == "POST":
        form = EvaluationForm(request.POST or None)
        if form.is_valid():
            form.save()
        return redirect('/leaderboard') #zum Leaderboard


def leaderboard_view(request):
    if request.method == "GET":
        queryset_evaluation = (Evaluation.objects.filter(game_id=123456).values('evaluation_player_1',
                                                                                'evaluation_player_2',
                                                                                'evaluation_player_3'))

        context = {
            "evaluation_list" : queryset_evaluation
         }
    return render(request, "game/leaderboard.html",context)