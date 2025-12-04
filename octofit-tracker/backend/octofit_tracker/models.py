from django.db import models

class Team(models.Model):
    id = models.CharField(primary_key=True, max_length=24)
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)

class User(models.Model):
    id = models.CharField(primary_key=True, max_length=24)
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    team_id = models.CharField(max_length=24)
    is_superhero = models.BooleanField(default=True)

class Activity(models.Model):
    id = models.CharField(primary_key=True, max_length=24)
    user_id = models.CharField(max_length=24)
    type = models.CharField(max_length=100)
    duration = models.IntegerField(help_text='Duration in minutes')
    date = models.DateField()

class Workout(models.Model):
    id = models.CharField(primary_key=True, max_length=24)
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    suggested_for_ids = models.JSONField(default=list)

class Leaderboard(models.Model):
    id = models.CharField(primary_key=True, max_length=24)
    team_id = models.CharField(max_length=24)
    points = models.IntegerField(default=0)
    updated_at = models.DateTimeField(auto_now=True)
