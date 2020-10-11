from django import forms

from .models import Answer
from .models import Player
from .models import Settings

class AnswerForm(forms.ModelForm):
    S = Settings.objects.get(game_id=123456)
    P = Player.objects.get(game_id=123456)
    player_name = forms.CharField()
    game_id     = forms.IntegerField()
    answer_1    = forms.CharField(label=S.category_1,
                    widget=forms.TextInput(attrs={"placeholder": S.game_letter}))
    answer_2    = forms.CharField(label=S.category_2,
                    widget=forms.TextInput(attrs={"placeholder": S.game_letter}))
    answer_3    = forms.CharField(label=S.category_3,
                    widget=forms.TextInput(attrs={"placeholder": S.game_letter}))
    answer_4    = forms.CharField(label=S.category_4,
                    widget=forms.TextInput(attrs={"placeholder": S.game_letter}))
    answer_5    = forms.CharField(label=S.category_5,
                    widget=forms.TextInput(attrs={"placeholder": S.game_letter}))
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
