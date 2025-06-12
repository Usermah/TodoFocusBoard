from django.core.management.base import BaseCommand
from django.contrib.auth.models import User

class Command(BaseCommand):
    help = 'Create a superuser if it does not exist'

    def handle(self, *args, **kwargs):
        if not User.objects.filter(username='usama').exists():
            User.objects.create_superuser(
                username='usama',
                email='usama@gmail.com',
                password='usamaH@737!'
            )
            self.stdout.write(self.style.SUCCESS("✅ Superuser 'usama' created"))
        else:
            self.stdout.write(self.style.WARNING("⚠️ Superuser 'usama' already exists"))
