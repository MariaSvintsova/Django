from django.core.management import BaseCommand
from autentification.models import User


class Command(BaseCommand):

    def handle(self, *args, **options):
        user = User.objects.create(
            email='mariasvintsova@gmail.com',
            first_name='mariasvintsova',
            last_name='Gmail',
            is_stuff=True,
            is_superuser=True
        )
        user.set_password('123qwe456rty')
        user.save()