from django.apps import AppConfig


class CodesConfig(AppConfig):
    name = 'codes'

    def ready(self):
        from .signals import post_save_generate_code