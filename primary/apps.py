from django.apps import AppConfig
from . import views


class PrimaryConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'primary'
