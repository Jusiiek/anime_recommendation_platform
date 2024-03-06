from django.core.management.base import BaseCommand
from django.db.models import Q
from user.models import User, Role


class Command(BaseCommand):
    help = 'Add user with role if not in db'

    def add_arguments(self, parser):
        parser.add_argument('--username', type=str)
        parser.add_argument('--email', type=str)
        parser.add_argument('--role', type=str)
        parser.add_argument('--first_name', default="", type=str)
        parser.add_argument('--last_name', default="", type=str)
        parser.add_argument('--is_superuser', default=False, type=bool)
        parser.add_argument('--is_staff', default=False, type=bool)
        parser.add_argument('--password', default="", type=str)

    def handle(self, *args, **options):
        email = options['email']
        username = options['username']
        user_qs = User.objects.filter(Q(email=email) | Q(username=username))
        if user_qs:
            self.stdout.write(self.style.SUCCESS('User already in db'))
            return
        user = User.objects.create(
            username=options['username'],
            email=options['email'],
            first_name=options['first_name'],
            last_name=options['last_name'],
            is_superuser=options['is_superuser'],
            is_staff=options['is_staff'],
        )
        user.set_password(options['password'])
        role = Role.objects.get(name=options['role'])
        user.set_role(role)
        user.save()

        self.stdout.write(self.style.SUCCESS('Successfully created user'))
