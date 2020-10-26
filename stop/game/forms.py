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
    answer_1    = forms.CharField(label="S.category_1",
                    widget=forms.TextInput(attrs={"placeholder": "S.game_letter"}))
    answer_2    = forms.CharField(label="S.category_2",
                    widget=forms.TextInput(attrs={"placeholder": "S.game_letter"}))
    answer_3    = forms.CharField(label="S.category_3",
                    widget=forms.TextInput(attrs={"placeholder": "S.game_letter"}))
    answer_4    = forms.CharField(label="S.category_4",
                    widget=forms.TextInput(attrs={"placeholder": "S.game_letter"}))
    answer_5    = forms.CharField(label="S.category_5",
                    widget=forms.TextInput(attrs={"placeholder": "S.game_letter"}))
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
    CHOICES = (('1', '1 Right'), ('2', '2 Right'),('3', '3 Right'),('4', '4 Right'),('5', '5 Right'),)
    evaluation_player_1 = forms.ChoiceField(choices=CHOICES)
    evaluation_player_2 = forms.ChoiceField(choices=CHOICES)
    evaluation_player_3 = forms.ChoiceField(choices=CHOICES)
    class Meta:
        model = Evaluation
        fields = [
            'game_id',
            'evaluation_player_1',
            'evaluation_player_2',
            'evaluation_player_3'
        ]