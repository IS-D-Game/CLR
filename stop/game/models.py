#A model is the single, definitive source of information about your data.
# It contains the essential fields and behaviors of the data you’re storing.
# Generally, each model maps to a single database table.
from django.db import models

# Create your models here.
class Answer(models.Model):
    answer_1 = models.CharField(max_length=200)
    answer_2 = models.CharField(max_length=200)
    answer_3 = models.CharField(max_length=200)
    answer_4 = models.CharField(max_length=200)
    answer_5 = models.CharField(max_length=200)
    game_id  = models.BigIntegerField()
    player_name = models.CharField(max_length=20)



class Player(models.Model):
    player_name = models.CharField(max_length=20)
    game_id = models.BigIntegerField()


class Settings(models.Model):
    number_of_players   = models.BigIntegerField()
    game_time_in_s      = models.BigIntegerField()
    game_letter         = models.CharField(max_length=1)
    game_id             = models.BigIntegerField()
    category_1          = models.CharField(max_length=50)
    category_2          = models.CharField(max_length=50)
    category_3          = models.CharField(max_length=50)
    category_4          = models.CharField(max_length=50)
    category_5          = models.CharField(max_length=50)

class Evaluation(models.Model):
    game_id  = models.BigIntegerField()
    evaluation_player_1 = models.CharField(max_length=50)
    evaluation_player_2 = models.CharField(max_length=50)
    evaluation_player_3 = models.CharField(max_length=50)
    evaluation_player_4 = models.CharField(max_length=50)
    evaluation_player_5 = models.CharField(max_length=50)
    player_name = models.CharField(max_length=20)
