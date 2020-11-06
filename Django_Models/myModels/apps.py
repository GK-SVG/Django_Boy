from django.apps import AppConfig


class MymodelsConfig(AppConfig):
    name = 'myModels'
    def ready(self):
        import myModels.signals