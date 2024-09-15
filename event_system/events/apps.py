from django.apps import AppConfig

class EventsConfig(AppConfig):
    name = 'events'

    def ready(self):
        # Import the signals module
        import events.signals