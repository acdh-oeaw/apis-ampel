from django.apps import AppConfig


class ApisAmpelConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apis_ampel'


    #could overwrite ready method here to run code when app is fully loaded
