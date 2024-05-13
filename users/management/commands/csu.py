from django.core.management import BaseCommand
from users.models import User


class Command(BaseCommand):

    def handle(self, *args, **options):
        user = User.objects.create(
            email='mariasvintsova123@gmail.com',
            is_stuff=True,
            is_superuser=True,
            phone='89012345678',
            country='Russia'
        )
        user.set_password('123qwe456rty')
        user.save()
