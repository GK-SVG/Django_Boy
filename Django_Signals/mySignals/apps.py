from django.apps import AppConfig


class MysignalsConfig(AppConfig):
    name = 'mySignals'

    def ready(self):
        import mySignals.signals