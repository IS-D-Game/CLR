from django import forms
import random
import string
from .models import Answer
from .models import Player
from .models import Settings
from .models import Evaluation

class SettingsForm(forms.ModelForm):
    # game_id     = forms.IntegerField()
    CHOICES_Players = (('3','3'),('4','4'),('5','5'))
    number_of_players = forms.ChoiceField(choices=CHOICES_Players, label='Number of Players')
    game_time_in_s = forms.IntegerField(label='Gametime in sec.')
    game_letter = forms.CharField(label='Letter')
    CHOICES_People = (('Musician', 'Musician'), ('Band', 'Band'),('Hollywood-Star', 'Hollywood-Star'),('Athlete', 'Athlete'),('Politician', 'Politician'),)
    CHOICES_Geography = (('City', 'City'), ('Country', 'Country'), ('River', 'River'), ('Lake', 'Lake'),('Mountain', 'Mountain'),)
    CHOICES_Food = (('Meal', 'Meal'), ('Liquor', 'Liquor'), ('Candy', 'Candy'), ('Fruit', 'Fruit'), ('Vegetables', 'Vegetables'),)
    CHOICES_Nature = (('Animal', 'Animal'), ('Dog-Breed', 'Dog-Breed'), ('Fish', 'Fish'), ('Bird', 'Bird'), ('Plant', 'Plant'),)
    CHOICES_Others = (('Movie', 'Movie'), ('Series', 'Series'), ('Cosmetic-Brand', 'Cosmetic-Brand'), ('Car-Brand', 'Car-Brand'), ('Clothing-Brand', 'Clothing-Brand'),)
    category_1          = forms.ChoiceField(choices=CHOICES_People, label="People")
    category_2          = forms.ChoiceField(choices=CHOICES_Geography, label="Geography")
    category_3          = forms.ChoiceField(choices=CHOICES_Food, label="Food")
    category_4          = forms.ChoiceField(choices=CHOICES_Nature, label="Nature")
    category_5          = forms.ChoiceField(choices=CHOICES_Others, label="Others")
    game_id = forms.CharField(label = "Game ID")
    class Meta:
        model = Settings
        fields = [
            'number_of_players',
            'game_time_in_s',
            'game_letter',
            'category_1',
            'category_2',
            'category_3',
            'category_4',
            'category_5',
            'game_id',
        ]


class AnswerForm(forms.ModelForm):
    player_name = forms.CharField(widget=forms.HiddenInput())
    game_id     = forms.IntegerField(widget=forms.HiddenInput())
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
    game_id     = forms.IntegerField(widget=forms.HiddenInput())
    player_name = forms.CharField(widget=forms.HiddenInput())
    CHOICES = (('0', '0 Right'), ('1', '1 Right'), ('2', '2 Right'),('3', '3 Right'),('4', '4 Right'),('5', '5 Right'),)
    evaluation_player_1 = forms.ChoiceField(choices=CHOICES)
    evaluation_player_2 = forms.ChoiceField(choices=CHOICES)
    evaluation_player_3 = forms.ChoiceField(choices=CHOICES)
    evaluation_player_4 = forms.ChoiceField(choices=CHOICES)
    evaluation_player_5 = forms.ChoiceField(choices=CHOICES)
    class Meta:
        model = Evaluation
        fields = [
            'game_id',
            'player_name',
            'evaluation_player_1',
            'evaluation_player_2',
            'evaluation_player_3',
            'evaluation_player_4',
            'evaluation_player_5'
        ]


