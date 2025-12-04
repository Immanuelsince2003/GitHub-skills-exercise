from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Workout, Leaderboard
from django.utils import timezone

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        from django.conf import settings
        import pymongo
        from bson.objectid import ObjectId
        client = pymongo.MongoClient(settings.DATABASES['default']['CLIENT']['host'])
        db = client[settings.DATABASES['default']['NAME']]
        # Clear collections

        for coll in ['activities', 'workouts', 'leaderboards', 'users', 'teams']:
            db[coll].delete_many({})


        # Insert teams
        marvel_id = str(ObjectId())
        dc_id = str(ObjectId())

        db['teams'].insert_many([
            {'_id': marvel_id, 'name': 'Marvel', 'description': 'Marvel Superheroes'},
            {'_id': dc_id, 'name': 'DC', 'description': 'DC Superheroes'}
        ])

        # Insert users
        users = [
            {'_id': str(ObjectId()), 'name': 'Spider-Man', 'email': 'spiderman@marvel.com', 'team_id': marvel_id, 'is_superhero': True},
            {'_id': str(ObjectId()), 'name': 'Iron Man', 'email': 'ironman@marvel.com', 'team_id': marvel_id, 'is_superhero': True},
            {'_id': str(ObjectId()), 'name': 'Wonder Woman', 'email': 'wonderwoman@dc.com', 'team_id': dc_id, 'is_superhero': True},
            {'_id': str(ObjectId()), 'name': 'Batman', 'email': 'batman@dc.com', 'team_id': dc_id, 'is_superhero': True},
        ]

        db['users'].insert_many(users)

        # Insert activities
        activities = [
            {'_id': str(ObjectId()), 'user_id': users[0]['_id'], 'type': 'Running', 'duration': 30, 'date': '2025-12-04'},
            {'_id': str(ObjectId()), 'user_id': users[1]['_id'], 'type': 'Cycling', 'duration': 45, 'date': '2025-12-04'},
            {'_id': str(ObjectId()), 'user_id': users[2]['_id'], 'type': 'Swimming', 'duration': 60, 'date': '2025-12-04'},
            {'_id': str(ObjectId()), 'user_id': users[3]['_id'], 'type': 'Yoga', 'duration': 20, 'date': '2025-12-04'},
        ]

        db['activities'].insert_many(activities)

        # Insert workouts
        workout1_id = str(ObjectId())
        workout2_id = str(ObjectId())

        db['workouts'].insert_many([
            {'_id': workout1_id, 'name': 'Cardio Blast', 'description': 'High intensity cardio', 'suggested_for_ids': [users[0]['_id'], users[2]['_id']]},
            {'_id': workout2_id, 'name': 'Strength Training', 'description': 'Build muscle', 'suggested_for_ids': [users[1]['_id'], users[3]['_id']]},
        ])

        # Insert leaderboards

        db['leaderboards'].insert_many([
            {'_id': str(ObjectId()), 'team_id': marvel_id, 'points': 150, 'updated_at': '2025-12-04T00:00:00Z'},
            {'_id': str(ObjectId()), 'team_id': dc_id, 'points': 120, 'updated_at': '2025-12-04T00:00:00Z'},
        ])

        # Create unique index on email

        db['users'].create_index([('email', 1)], unique=True)

        self.stdout.write(self.style.SUCCESS('Test data populated successfully.'))
