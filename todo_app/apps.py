# from django.apps import AppConfig


# class TodoAppConfig(AppConfig):
#     default_auto_field = 'django.db.models.BigAutoField'
#     name = 'todo_app'


from django.apps import AppConfig
from django.contrib.auth.models import User
from django.db.utils import OperationalError

class TodoAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'todo_app'

    def ready(self):
        try:
            if not User.objects.filter(username='usama').exists():
                User.objects.create_superuser(
                    username='usama',
                    email='usama@gmail.com',
                    password='usamaH@737!'
                )
                print("✅ Superuser 'usama' created")
        except OperationalError:
            # Happens during migrations before DB is ready
            pass
