from rest_framework import serializers
from .models import Event, Registration, Participant


class ParticipantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Participant
        fields = ['id', 'uuid', 'name', 'age']


class RegistrationSerializer(serializers.ModelSerializer):
    participants = ParticipantSerializer(many=True, read_only=True)  # Nested participants

    class Meta:
        model = Registration
        fields = ['id', 'uuid', 'event', 'registered_at', 'email', 'participants']


class EventSerializer(serializers.ModelSerializer):
    registrations = RegistrationSerializer(many=True, read_only=True)  # Nested registrations
    class Meta:
        model = Event
        fields = ['id', 'uuid', 'name', 'description', 'date', 'location', 'created_at', 'registrations']
