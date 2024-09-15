import uuid
from django.db import models
from .tasks import process_long_running_task
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth.models import User  # Assuming organizer is a User


# Create your models here.
class Event(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    name = models.CharField(max_length=255)
    description = models.TextField()
    date = models.DateField()
    location = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    organizer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='organized_events')  # ForeignKey to User


    def __str__(self):
        return self.name


class Registration(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)  # Add UUID as additional field
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='registrations')
    name = models.CharField(max_length=255)
    email = models.EmailField()
    registered_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name} - {self.event.name}'


class Participant(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    registration = models.ForeignKey(Registration, on_delete=models.CASCADE, related_name='participants')
    name = models.CharField(max_length=255)
    age = models.IntegerField()

    def __str__(self):
        return f'{self.name} ({self.registration.event.name})'
