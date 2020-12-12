from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
import random
import string
from .forms import SettingsForm
from .forms import AnswerForm
from .forms import PlayerForm
from .forms import EvaluationForm
from .models import Player
from .models import Answer
from .models import Settings
from .models import Evaluation
from django import forms

"""
Start Page View
    - View to choose to enter a game or host a game
"""
def start_page_view(request):
    return render(request, "game/start_page.html")

"""
Game Create View
    - View to fill out the Settings Form
    - game_time_in_s is set to 30, but editable by host
    - game_id is a random 6-digits number, not editable
    - game_letter is a set random letter out of a ascii_uppercase string, but editable by host
    - Primary Key is passed to URL
"""
def game_create_view(request):
    if request.method == "GET":
        form = SettingsForm()
        form.fields['game_time_in_s'].initial = 30
        form.fields['game_id'].widget = forms.TextInput(attrs={'readonly': 'readonly'})
        form.fields['game_id'].initial = random.randint(100000, 999999)
        list_letters = string.ascii_uppercase
        form.fields['game_letter'].initial = random.choice(list_letters)
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
        return redirect('/player/'+form.data["game_id"], context)

"""
Player Create View
    - View to fill out the Player Form
    - Primary Keys are passed to URL
"""
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
        context = {
            'form': form,
        }
        return redirect('/game/'+form.data['player_name']+'/'+form.data['game_id'], context)

"""
Player Create View 2
    - View for the host who created the game, auto filled game_id
    - Player only has to type in the player_name
    - Get the Model based on the game_id and prefill with instance
    - Primary Keys are passed to URL
"""
def player_create_view_2(request, game_id):
    if request.method == "GET":
        # Get Model Data
        obj = Settings.objects.get(game_id=game_id)
        # Fill with instance
        form = PlayerForm(request.POST or None, instance=obj)
        form.fields["game_id"].widget = forms.TextInput(attrs={"readonly": "readonly"})
        context = {
            'form': form
        }
        return render(request, "game/player_create.html", context)
    elif request.method == "POST":
        form = PlayerForm(request.POST or None)
        form.save()
        context = {
            'form': form,
        }

        return redirect('/game/'+form.data['player_name']+'/'+form.data['game_id'], context)

"""
Game View
    - View for the players to fill out the game answers
    - Get the SettingsModel based on the game_id to show categories and use the correct game time
    - Get the PlayerModel based on the game_id and player_name, to autofill primary keys
    - Primary keys are passed to URL
"""
def game_view(request, game_id, player_name):
    if request.method == "GET":
        # Get Model Data
        obj = Player.objects.get(player_name=player_name, game_id=game_id)
        S = Settings.objects.get(game_id=obj.game_id)
        # Fill with instance
        form = AnswerForm(request.POST or None, instance = obj)
        # Form Design
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
        # Context objects to send
        # Time for autosave form and auto redirect (*1000 for milliseconds /+ 1000 to add a second delay)
        game_time = S.game_time_in_s * 1000 + 1000
        # game time used for timer and progress bar
        game_time_s = S.game_time_in_s
        context = {
            "form" : form,
            "game_time" : game_time,
            "game_time_s" : game_time_s
         }
        return render(request, "game/game.html", context)
    elif request.method == "POST":
        form = AnswerForm(request.POST or None)
        if form.is_valid():
            form.save()
        context = {
            'form': form,
        }
        return redirect('/evaluation/'+form.data['player_name']+'/'+form.data['game_id'], context)

"""
Evaluation View
    - View for the players to evaluate each others points
    - Get the SettingsModel based on the game_id to show player names in the form
    - Get the AnswerModel based on the game_id and player_name, to show answers
    - Use an if/elif logic which hides the evaluation fields based on number of players
    - Primary keys are passed to URL
"""
def evaluation_view(request, game_id, player_name):
    if request.method == "GET":
        # Get Model Data
        obj = Answer.objects.get(player_name=player_name, game_id=game_id)
        S = Settings.objects.get(game_id=obj.game_id)
        queryset_player = Answer.objects.filter(game_id=obj.game_id).values_list('player_name', flat=True)
        # Fill with instance
        form = EvaluationForm(request.POST or None, instance=obj)
        # Form Design (slice string [2:-2] to remove ["/"] from query element)
        form.fields['evaluation_player_1'].label = str(list(queryset_player[:1]))[2:-2]
        form.fields['evaluation_player_2'].label = str(list(queryset_player[1:2]))[2:-2]
        form.fields['evaluation_player_3'].label = str(list(queryset_player[2:3]))[2:-2]
        form.fields['evaluation_player_4'].label = str(list(queryset_player[3:4]))[2:-2]
        form.fields['evaluation_player_5'].label = str(list(queryset_player[4:5]))[2:-2]
        # Context objects to send
        queryset_category = (Settings.objects.filter(
            game_id=obj.game_id).values('category_1', 'category_2', 'category_3', 'category_4','category_5'))
        queryset = (Answer.objects.filter(
            game_id=obj.game_id).values('player_name', 'answer_1', 'answer_2', 'answer_3','answer_4', 'answer_5'))
        # Form to evaluate equal to player number if/elif logic
        if S.number_of_players == 3:
            # Form Design for 3 Players
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
            # Form Design for 4 Players
            form.fields['evaluation_player_5'].widget = forms.HiddenInput()
            form.fields['evaluation_player_5'].initial = '0'
            context = {
                "form": form,
                "answer_list": queryset,
                "category_list": queryset_category
            }
        elif S.number_of_players == 5:
            # Form Design for 5 Players = no hidden fields
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


"""
Leaderboard View
    - View for the players to see the final points
    - Get the SettingsModel based on the game_id
    - Get the AnswerModel based on the game_id and player_name
    - Get the EvaluationModel based on the game_id
    - Use an if/elif logic for the points calculation based on number of players
    - Primary keys are passed to URL
"""
def leaderboard_view(request, player_name, game_id):
    if request.method == "GET":
        # Get Model Data
        obj = Answer.objects.get(player_name=player_name, game_id=game_id)
        S = Settings.objects.filter(game_id=obj.game_id).get()
        # Context object to send
        queryset_player_name = Answer.objects.filter(game_id=obj.game_id).values('player_name')
        # logic to count points per player
        if S.number_of_players == 3:
            p1 = Evaluation.objects.filter(game_id=obj.game_id).values_list('evaluation_player_1', flat=True)
            e1 = sum(list(map(int, p1[:1])) + list(map(int, p1[1:2])) + list(map(int, p1[2:3])) + list(map(int, p1[3:4])) + list(map(int, p1[4:5])))
            p2 = Evaluation.objects.filter(game_id=obj.game_id).values_list('evaluation_player_2', flat=True)
            e2 = sum(list(map(int, p2[:1])) + list(map(int, p2[1:2])) + list(map(int, p2[2:3])) + list(map(int, p2[3:4])) + list(map(int, p2[4:5])))
            p3 = Evaluation.objects.filter(game_id=obj.game_id).values_list('evaluation_player_3', flat=True)
            e3 = sum(list(map(int, p3[:1])) + list(map(int, p3[1:2])) + list(map(int, p3[2:3])) + list(map(int, p3[3:4])) + list(map(int, p3[4:5])))
            context = {
                "e1": e1,
                "e2": e2 ,
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


"""
Error Views
    - for Error 404
    - for Error 500
"""
def handler404(request, *args, **argv):
    return render(request, 'game/error.html', status=404)
def handler500(request, *args, **argv):
    return render(request, 'game/error.html', status=500)