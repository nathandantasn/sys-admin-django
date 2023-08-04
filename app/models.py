from django.db import models

# Create your models here.
# Django ORM

class Player (models.Model):
    name = models.CharField(max_length=50)
    initial_price = models.FloatField()

    def __str__(self):
        return self.name

class Team (models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class MyTeam (models.Model):
    players = models.ManyToManyField(Player)