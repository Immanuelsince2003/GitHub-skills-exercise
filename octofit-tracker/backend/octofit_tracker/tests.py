from django.test import TestCase
from .models import User, Team, Activity, Workout, Leaderboard

class ModelTests(TestCase):
    def setUp(self):
        self.team = Team.objects.create(name='Marvel', description='Marvel Superheroes')
        self.user = User.objects.create(name='Spider-Man', email='spiderman@marvel.com', team=self.team, is_superhero=True)
        self.activity = Activity.objects.create(user=self.user, type='Running', duration=30, date='2025-12-04')
        self.workout = Workout.objects.create(name='Cardio Blast', description='High intensity cardio')
        self.workout.suggested_for.add(self.user)
        self.leaderboard = Leaderboard.objects.create(team=self.team, points=100)

    def test_user_email_unique(self):
        with self.assertRaises(Exception):
            User.objects.create(name='Duplicate', email='spiderman@marvel.com', team=self.team)

    def test_team_membership(self):
        self.assertEqual(self.user.team.name, 'Marvel')

    def test_activity_creation(self):
        self.assertEqual(self.activity.type, 'Running')

    def test_workout_suggestion(self):
        self.assertIn(self.user, self.workout.suggested_for.all())

    def test_leaderboard_points(self):
        self.assertEqual(self.leaderboard.points, 100)
