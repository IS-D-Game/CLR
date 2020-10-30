from django import forms

from .models import Answer
from .models import Player
from .models import Settings
from .models import Evaluation

class AnswerForm(forms.ModelForm):
    # S = Settings.objects.get(game_id=123456)
    # P = Player.objects.get(player_name="Dominik")
    player_name = forms.CharField()
    game_id     = forms.IntegerField()
    answer_1    = forms.CharField()
    answer_2    = forms.CharField()
    answer_3    = forms.CharField()
    answer_4    = forms.CharField()
    answer_5    = forms.CharField()
    class Meta:
        model = Answer
        fields = [
            'player_name',
            'game_id',
            'answer_1',
            'answer_2',
            'answer_3',
            'answer_4',
            'answer_5',
        ]


class PlayerForm(forms.ModelForm):
    player_name = forms.CharField(label='Name',
                    widget=forms.TextInput(attrs={"placeholder": "Your Name"}))
    game_id = forms.IntegerField()

    class Meta:
        model = Player
        fields = [
            'player_name',
            'game_id',
        ]


class EvaluationForm(forms.ModelForm):
    game_id     = forms.IntegerField()
    player_name = forms.CharField()
    S = Settings.objects.get(game_id=222)
    CHOICES = (('1', '1 Right'), ('2', '2 Right'),('3', '3 Right'),('4', '4 Right'),('5', '5 Right'),)
    if S.number_of_players == 2:
        evaluation_player_1 = forms.ChoiceField(choices=CHOICES)
        evaluation_player_2 = forms.ChoiceField(choices=CHOICES)
        class Meta:
            model = Evaluation
            fields = [
                'game_id',
                'player_name',
                'evaluation_player_1',
                'evaluation_player_2'
            ]
    elif S.number_of_players == 3:
        evaluation_player_1 = forms.ChoiceField(choices=CHOICES)
        evaluation_player_2 = forms.ChoiceField(choices=CHOICES)
        evaluation_player_3 = forms.ChoiceField(choices=CHOICES)
        class Meta:
            model = Evaluation
            fields = [
                'game_id',
                'player_name',
                'evaluation_player_1',
                'evaluation_player_2',
                'evaluation_player_3'
            ]

    # evaluation_player_1 = forms.ChoiceField(choices=CHOICES)
    # evaluation_player_2 = forms.ChoiceField(choices=CHOICES)
    # evaluation_player_3 = forms.ChoiceField(choices=CHOICES)
