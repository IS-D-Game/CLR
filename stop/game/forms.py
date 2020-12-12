from django import forms
from .models import Answer
from .models import Player
from .models import Settings
from .models import Evaluation

"""
Settings Form:
    - Is used to store the game settings input to the Settings Model
    - game_id is used as primary key
    - Categories and number of players as a choice form
"""
class SettingsForm(forms.ModelForm):
    # Choices
    CHOICES_Players = (('3','3'),('4','4'),('5','5'))
    CHOICES_People = (('Musician', 'Musician'), ('Band', 'Band'),('Hollywood-Star', 'Hollywood-Star'),('Athlete', 'Athlete'),('Politician', 'Politician'),)
    CHOICES_Geography = (('City', 'City'), ('Country', 'Country'), ('River', 'River'), ('Lake', 'Lake'),('Mountain', 'Mountain'),)
    CHOICES_Food = (('Meal', 'Meal'), ('Liquor', 'Liquor'), ('Candy', 'Candy'), ('Fruit', 'Fruit'), ('Vegetables', 'Vegetables'),)
    CHOICES_Nature = (('Animal', 'Animal'), ('Dog-Breed', 'Dog-Breed'), ('Fish', 'Fish'), ('Bird', 'Bird'), ('Plant', 'Plant'),)
    CHOICES_Others = (('Movie', 'Movie'), ('Series', 'Series'), ('Cosmetic-Brand', 'Cosmetic-Brand'), ('Car-Brand', 'Car-Brand'), ('Clothing-Brand', 'Clothing-Brand'),)
    # Parameters
    number_of_players = forms.ChoiceField(
        choices=CHOICES_Players,
        label='Select the number of players')
    game_time_in_s = forms.IntegerField(
        label='Enter the preferred game time in seconds')
    game_letter = forms.CharField(
        label='Enter the preferred game letter')
    category_1 = forms.ChoiceField(
        choices=CHOICES_People,
        label="Select the preferred game category on the theme of people")
    category_2 = forms.ChoiceField(
        choices=CHOICES_Geography,
        label="Select the preferred game category on the theme of geography")
    category_3 = forms.ChoiceField(
        choices=CHOICES_Food,
        label="Select the preferred game category on the theme of food")
    category_4 = forms.ChoiceField(
        choices=CHOICES_Nature,
        label="Select the preferred game category on the theme of nature.")
    category_5 = forms.ChoiceField(
        choices=CHOICES_Others,
        label="Select the preferred game category on the mixes theme")
    # Primary Key
    game_id = forms.CharField(
        label = "Game ID")
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

"""
Player Form:
    - Is used to store the player data to the Player Model
    - game_id and player_name is used as primary key
"""
class PlayerForm(forms.ModelForm):
    # Primary Keys
    player_name = forms.CharField(
        label='Name',
        widget=forms.TextInput(
            attrs={"placeholder": "Your Name"}))
    game_id = forms.IntegerField(
        label='Game-ID')
    class Meta:
        model = Player
        fields = [
            'player_name',
            'game_id',
        ]

"""
Answer Form:
    - Is used to store the game answers to the Answer Model
    - game_id and player_name is used as primary key
"""
class AnswerForm(forms.ModelForm):
    answer_1 = forms.CharField()
    answer_2 = forms.CharField()
    answer_3 = forms.CharField()
    answer_4 = forms.CharField()
    answer_5 = forms.CharField()
    # Primary Keys (hidden and autofill over view)
    player_name = forms.CharField(widget=forms.HiddenInput())
    game_id = forms.IntegerField(widget=forms.HiddenInput())
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


"""
Evaluation Form:
    - Is used to store the game points per player to the Evaluation Model
    - game_id and player_name is used as primary key
    - Evaluation as a choice form, to choice reached points
"""
class EvaluationForm(forms.ModelForm):
    # Choices
    CHOICES = (('0', '0 Right'), ('1', '1 Right'), ('2', '2 Right'),('3', '3 Right'),('4', '4 Right'),('5', '5 Right'),)
    # Fields
    evaluation_player_1 = forms.ChoiceField(choices=CHOICES)
    evaluation_player_2 = forms.ChoiceField(choices=CHOICES)
    evaluation_player_3 = forms.ChoiceField(choices=CHOICES)
    evaluation_player_4 = forms.ChoiceField(choices=CHOICES)
    evaluation_player_5 = forms.ChoiceField(choices=CHOICES)
    # Primary Keys (hidden and autofill over view)
    game_id = forms.IntegerField(widget=forms.HiddenInput())
    player_name = forms.CharField(widget=forms.HiddenInput())
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


