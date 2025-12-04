
from djongo import models


class Team(models.Model):
    id = models.ObjectIdField(primary_key=True, db_column='_id')
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)

    class Meta:
        db_table = 'teams'


class User(models.Model):
    id = models.ObjectIdField(primary_key=True, db_column='_id')
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    team_id = models.CharField(max_length=24)
    is_superhero = models.BooleanField(default=True)

    class Meta:
        db_table = 'users'


class Activity(models.Model):
    id = models.ObjectIdField(primary_key=True, db_column='_id')
    user_id = models.CharField(max_length=24)
    type = models.CharField(max_length=100)
    duration = models.IntegerField(help_text='Duration in minutes')
    date = models.DateField()

    class Meta:
        db_table = 'activities'


class Workout(models.Model):
    id = models.ObjectIdField(primary_key=True, db_column='_id')
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    suggested_for_ids = models.JSONField(default=list)

    class Meta:
        db_table = 'workouts'


class Leaderboard(models.Model):
    id = models.ObjectIdField(primary_key=True, db_column='_id')
    team_id = models.CharField(max_length=24)
    points = models.IntegerField(default=0)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'leaderboards'
