from django.db import models


"""
Settings Model:
    - Is used to store the game settings parameter
    - game_id is used as primary key
"""
class Settings(models.Model):
    number_of_players = models.BigIntegerField()
    game_time_in_s = models.BigIntegerField()
    game_letter = models.CharField(max_length=1)
    category_1 = models.CharField(max_length=50)
    category_2 = models.CharField(max_length=50)
    category_3 = models.CharField(max_length=50)
    category_4 = models.CharField(max_length=50)
    category_5 = models.CharField(max_length=50)
    # PK
    game_id = models.BigIntegerField()

"""
Player Model:
    - Is used to store each player per game
    - game_id and player_name is used as primary key
"""
class Player(models.Model):
    # PK
    player_name = models.CharField(max_length=20)
    game_id = models.BigIntegerField()

"""
Answer Model:
    - Is used to store each game answer per category from each player
    - game_id and player_name is used as primary key (autofilled, hidden objects)
"""
class Answer(models.Model):
    answer_1 = models.CharField(max_length=200)
    answer_2 = models.CharField(max_length=200)
    answer_3 = models.CharField(max_length=200)
    answer_4 = models.CharField(max_length=200)
    answer_5 = models.CharField(max_length=200)
    # PK
    game_id = models.BigIntegerField()
    player_name = models.CharField(max_length=20)

"""
Evaluation Model:
    - Is used to store the reached game points per player
    - game_id and player_name is used as primary key (autofilled, hidden objects)
"""
class Evaluation(models.Model):
    evaluation_player_1 = models.CharField(max_length=50)
    evaluation_player_2 = models.CharField(max_length=50)
    evaluation_player_3 = models.CharField(max_length=50)
    evaluation_player_4 = models.CharField(max_length=50)
    evaluation_player_5 = models.CharField(max_length=50)
    # PK
    player_name = models.CharField(max_length=20)
    game_id = models.BigIntegerField()
