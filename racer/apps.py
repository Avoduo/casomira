from django.apps import AppConfig


class RacerConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'racer'

class ZavodConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'zavod'