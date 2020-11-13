from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
import json
from .forms import SettingsForm
from .forms import AnswerForm
from .forms import PlayerForm
from .forms import EvaluationForm
from .models import Player
from .models import Answer
from .models import Settings
from .models import Evaluation
from django import forms


# Create your views here.
def game_view(request, game_id, player_name):
    if request.method == "GET":
        obj = Player.objects.get(player_name=player_name, game_id=game_id)
        queryset_category = (Settings.objects.filter(game_id=obj.game_id).values('category_1', 'category_2', 'category_3', 'category_4',
                                                                 'category_5'))
        S = Settings.objects.get(game_id=obj.game_id)
        form = AnswerForm(request.POST or None, instance = obj)
        form.fields['answer_1'].label = S.category_1
        form.fields['answer_2'].label = S.category_2
        form.fields['answer_3'].label = S.category_3
        form.fields['answer_4'].label = S.category_4
        form.fields['answer_5'].label = S.category_5
        form.fields['answer_1'].initial = S.game_letter
        form.fields['answer_2'].initial = S.game_letter
        form.fields['answer_3'].initial = S.game_letter
        form.fields['answer_4'].initial = S.game_letter
        form.fields['answer_5'].initial = S.game_letter

        context = {
            "form" : form,
            "settings" : queryset_category
         }
        return render(request, "game/game.html", context)
    elif request.method == "POST":
        form = AnswerForm(request.POST or None)
        if form.is_valid():
            form.save()
        context = {
            'form': form,
        }
        return redirect('/evaluation/'+form.data['player_name']+'/'+form.data['game_id'], context) #zu auswertung


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
    if request.method == "GET":
        form = SettingsForm()
        form.fields['game_id'].widget = forms.TextInput(attrs={'readonly': 'readonly'})
        context = {
            'form': form
        }
        return render(request, "game/game_create.html", context)
    elif request.method == "POST":
        form = SettingsForm(request.POST or None)
        if form.is_valid():
            form.save()
        context = {
            'form': form,
         }
        return redirect('/player/', context)



def evaluation_view(request, game_id, player_name):
    if request.method == "GET":
        obj = Answer.objects.get(player_name=player_name, game_id=game_id)
        queryset_category = (Settings.objects.filter(game_id=obj.game_id).values('category_1', 'category_2', 'category_3', 'category_4',
                                                                 'category_5'))
        queryset = (Answer.objects.filter(game_id=obj.game_id).values('player_name', 'answer_1', 'answer_2', 'answer_3',
                                                          'answer_4', 'answer_5'))
        form = EvaluationForm(request.POST or None, instance=obj)

        S = Settings.objects.get(game_id=obj.game_id)
        if S.number_of_players == 3:
            form.fields['evaluation_player_4'].widget = forms.HiddenInput()
            form.fields['evaluation_player_5'].widget = forms.HiddenInput()
            form.fields['evaluation_player_4'].initial = '0'
            form.fields['evaluation_player_5'].initial = '0'

            context = {
                "form": form,
                "answer_list": queryset,
                "category_list": queryset_category
            }

        elif S.number_of_players == 4:
            form.fields['evaluation_player_5'].widget = forms.HiddenInput()
            form.fields['evaluation_player_5'].initial = '0'

            context = {
                "form": form,
                "answer_list": queryset,
                "category_list": queryset_category
            }

        elif S.number_of_players == 5:

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
        context = {
            'form': form,
        }
        return redirect('/leaderboard/' + form.data['player_name'] + '/' + form.data['game_id'], context)



def leaderboard_view(request, player_name, game_id):
    if request.method == "GET":
        obj = Answer.objects.get(player_name=player_name, game_id=game_id)
        S = Settings.objects.filter(game_id=obj.game_id).get()

        queryset_player_name = Answer.objects.filter(game_id=obj.game_id).values('player_name')

        if S.number_of_players == 3:
            p1 = Evaluation.objects.filter(game_id=obj.game_id).values_list('evaluation_player_1', flat=True)
            e1 = sum(list(map(int, p1[:1])) + list(map(int, p1[1:2])) + list(map(int, p1[2:3])) + list(map(int, p1[3:4])) + list(map(int, p1[4:5])))
            p2 = Evaluation.objects.filter(game_id=obj.game_id).values_list('evaluation_player_2', flat=True)
            e2 = sum(list(map(int, p2[:1])) + list(map(int, p2[1:2])) + list(map(int, p2[2:3])) + list(map(int, p2[3:4])) + list(map(int, p2[4:5])))
            p3 = Evaluation.objects.filter(game_id=obj.game_id).values_list('evaluation_player_3', flat=True)
            e3 = sum(list(map(int, p3[:1])) + list(map(int, p3[1:2])) + list(map(int, p3[2:3])) + list(map(int, p3[3:4])) + list(map(int, p3[4:5])))
            context = {
                "e1": e1,
                "e2": e2,
                "e3": e3,
                "queryset_player_name": queryset_player_name
            }


        elif S.number_of_players == 4:
            p1 = Evaluation.objects.filter(game_id=obj.game_id).values_list('evaluation_player_1', flat=True)
            e1 = sum(list(map(int, p1[:1])) + list(map(int, p1[1:2])) + list(map(int, p1[2:3])) + list(map(int, p1[3:4])) + list(map(int, p1[4:5])))
            p2 = Evaluation.objects.filter(game_id=obj.game_id).values_list('evaluation_player_2', flat=True)
            e2 = sum(list(map(int, p2[:1])) + list(map(int, p2[1:2])) + list(map(int, p2[2:3])) + list(map(int, p2[3:4])) + list(map(int, p2[4:5])))
            p3 = Evaluation.objects.filter(game_id=obj.game_id).values_list('evaluation_player_3', flat=True)
            e3 = sum(list(map(int, p3[:1])) + list(map(int, p3[1:2])) + list(map(int, p3[2:3])) + list(map(int, p3[3:4])) + list(map(int, p3[4:5])))
            p4 = Evaluation.objects.filter(game_id=obj.game_id).values_list('evaluation_player_4', flat=True)
            e4 = sum(list(map(int, p4[:1])) + list(map(int, p4[1:2])) + list(map(int, p3[2:3])) + list(map(int, p4[3:4])) + list(map(int, p4[4:5])))
            context = {
                "e1": e1,
                "e2": e2,
                "e3": e3,
                "e4": e4,
                "queryset_player_name": queryset_player_name
            }


        elif S.number_of_players == 5:
            p1 = Evaluation.objects.filter(game_id=obj.game_id).values_list('evaluation_player_1', flat=True)
            e1 = sum(list(map(int, p1[:1])) + list(map(int, p1[1:2])) + list(map(int, p1[2:3])) + list(
                map(int, p1[3:4])) + list(map(int, p1[4:5])))
            p2 = Evaluation.objects.filter(game_id=obj.game_id).values_list('evaluation_player_2', flat=True)
            e2 = sum(list(map(int, p2[:1])) + list(map(int, p2[1:2])) + list(map(int, p2[2:3])) + list(
                map(int, p2[3:4])) + list(map(int, p2[4:5])))
            p3 = Evaluation.objects.filter(game_id=obj.game_id).values_list('evaluation_player_3', flat=True)
            e3 = sum(list(map(int, p3[:1])) + list(map(int, p3[1:2])) + list(map(int, p3[2:3])) + list(
                map(int, p3[3:4])) + list(map(int, p3[4:5])))
            p4 = Evaluation.objects.filter(game_id=obj.game_id).values_list('evaluation_player_4', flat=True)
            e4 = sum(list(map(int, p4[:1])) + list(map(int, p4[1:2])) + list(map(int, p3[2:3])) + list(
                map(int, p4[3:4])) + list(map(int, p4[4:5])))
            p5 = Evaluation.objects.filter(game_id=obj.game_id).values_list('evaluation_player_5', flat=True)
            e5 = sum(list(map(int, p5[:1])) + list(map(int, p5[1:2])) + list(map(int, p5[2:3])) + list(
                map(int, p5[3:4])) + list(map(int, p5[4:5])))

            context = {
                "e1": e1,
                "e2": e2,
                "e3": e3,
                "e4": e4,
                "e5": e5,
                "queryset_player_name": queryset_player_name
            }

    return render(request, "game/leaderboard.html",context)