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
        for coll in ['activity', 'workout', 'leaderboard', 'user', 'team']:
            db[coll].delete_many({})

        # Insert teams
        marvel_id = str(ObjectId())
        dc_id = str(ObjectId())
        db['team'].insert_many([
            {'id': marvel_id, 'name': 'Marvel', 'description': 'Marvel Superheroes'},
            {'id': dc_id, 'name': 'DC', 'description': 'DC Superheroes'}
        ])

        # Insert users
        users = [
            {'id': str(ObjectId()), 'name': 'Spider-Man', 'email': 'spiderman@marvel.com', 'team_id': marvel_id, 'is_superhero': True},
            {'id': str(ObjectId()), 'name': 'Iron Man', 'email': 'ironman@marvel.com', 'team_id': marvel_id, 'is_superhero': True},
            {'id': str(ObjectId()), 'name': 'Wonder Woman', 'email': 'wonderwoman@dc.com', 'team_id': dc_id, 'is_superhero': True},
            {'id': str(ObjectId()), 'name': 'Batman', 'email': 'batman@dc.com', 'team_id': dc_id, 'is_superhero': True},
        ]
        db['user'].insert_many(users)

        # Insert activities
        activities = [
            {'id': str(ObjectId()), 'user_id': users[0]['id'], 'type': 'Running', 'duration': 30, 'date': '2025-12-04'},
            {'id': str(ObjectId()), 'user_id': users[1]['id'], 'type': 'Cycling', 'duration': 45, 'date': '2025-12-04'},
            {'id': str(ObjectId()), 'user_id': users[2]['id'], 'type': 'Swimming', 'duration': 60, 'date': '2025-12-04'},
            {'id': str(ObjectId()), 'user_id': users[3]['id'], 'type': 'Yoga', 'duration': 20, 'date': '2025-12-04'},
        ]
        db['activity'].insert_many(activities)

        # Insert workouts
        workout1_id = str(ObjectId())
        workout2_id = str(ObjectId())
        db['workout'].insert_many([
            {'id': workout1_id, 'name': 'Cardio Blast', 'description': 'High intensity cardio', 'suggested_for_ids': [users[0]['id'], users[2]['id']]},
            {'id': workout2_id, 'name': 'Strength Training', 'description': 'Build muscle', 'suggested_for_ids': [users[1]['id'], users[3]['id']]},
        ])

        # Insert leaderboards
        db['leaderboard'].insert_many([
            {'id': str(ObjectId()), 'team_id': marvel_id, 'points': 150, 'updated_at': '2025-12-04T00:00:00Z'},
            {'id': str(ObjectId()), 'team_id': dc_id, 'points': 120, 'updated_at': '2025-12-04T00:00:00Z'},
        ])

        # Create unique index on email
        db['user'].create_index([('email', 1)], unique=True)

        self.stdout.write(self.style.SUCCESS('Test data populated successfully.'))
