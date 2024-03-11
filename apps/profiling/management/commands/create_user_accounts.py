from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from apps.profiling.models import UserProfile
from faker import Faker

class Command(BaseCommand):
    help = 'Create user accounts using Faker'

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help='Number of user accounts to create')

    def handle(self, *args, **options):
        fake = Faker()
        count = options['count']

        users = []
        profiles = []

        for _ in range(count):
            username = fake.user_name()
            email = fake.email()
            password = fake.password()

            user = User(username=(username+str(_)), email=email)
            users.append(user)

            profile = UserProfile(user=user, bio=fake.text(), location=fake.city(), birth_date=fake.date_of_birth())
            profiles.append(profile)

        User.objects.bulk_create(users)
        UserProfile.objects.bulk_create(profiles)


        self.stdout.write(self.style.SUCCESS(f'Successfully created {count} user accounts'))
