from django.contrib import admin
from .models import Event, Registration, Participant


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('id', 'uuid', 'name', 'description', 'date', 'location', 'created_at')
    search_fields = ('name', 'description', 'location')
    list_filter = ('date',)

@admin.register(Registration)
class RegistrationAdmin(admin.ModelAdmin):
    list_display = ('id', 'uuid', 'event', 'registered_at', 'email')
    search_fields = ('email', 'event__name')
    list_filter = ('event', 'registered_at')

@admin.register(Participant)
class ParticipantAdmin(admin.ModelAdmin):
    list_display = ('id', 'uuid', 'name', 'age')
    search_fields = ('name',)