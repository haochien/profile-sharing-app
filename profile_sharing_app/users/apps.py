from django.apps import AppConfig


class UsersConfig(AppConfig):
    # Customizing type of auto-created primary keys
    # https://docs.djangoproject.com/en/3.2/releases/3.2/#customizing-type-of-auto-created-primary-keys
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'users'

    def ready(self):
        import users.signals