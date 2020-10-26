from django.db import models

# Create your models here.
class Answer(models.Model):
    answer_1 = models.CharField(max_length=200)
    answer_2 = models.CharField(max_length=200)
    answer_3 = models.CharField(max_length=200)
    answer_4 = models.CharField(max_length=200)
    answer_5 = models.CharField(max_length=200)
    game_id  = models.BigIntegerField(max_length=6)
    player_name = models.CharField(max_length=20)



class Player(models.Model):
    player_name = models.CharField(max_length=20)
    game_id = models.BigIntegerField(max_length=6)


class Settings(models.Model):
    number_of_players   = models.BigIntegerField(max_length=1)
    game_time_in_s      = models.BigIntegerField(max_length=3)
    game_letter         = models.CharField(max_length=1)
    game_id             = models.BigIntegerField(max_length=6)
    category_1          = models.CharField(max_length=50)
    category_2          = models.CharField(max_length=50)
    category_3          = models.CharField(max_length=50)
    category_4          = models.CharField(max_length=50)
    category_5          = models.CharField(max_length=50)

class Evaluation(models.Model):
    game_id  = models.BigIntegerField(max_length=6)
    e1_1 = models.CharField(max_length=50)
    e1_2 = models.BooleanField()
    e1_3 = models.BooleanField()
