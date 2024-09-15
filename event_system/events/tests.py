from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from .models import Event, Participant, Registration
from django.contrib.auth.models import User
from datetime import datetime

class EventTestCase(TestCase):

    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.client.force_authenticate(user=self.user)

        self.participant = Participant.objects.create(name='John Doe', email='john@example.com')

        self.event_data = {
            'name': 'Bucky Conference',
            'date': '2024-09-15',
            'organizer': self.user.id,
        }

        self.registration_data = {
            'event': None,
            'participant': self.participant.id,
        }

    def test_create_event(self):
        response = self.client.post(reverse('event-list'), self.event_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Event.objects.count(), 1)
        self.assertEqual(Event.objects.get().name, 'Bucky Conference')

    def test_create_participant(self):
        participant_data = {
            'name': 'Jane Doe',
            'email': 'jane@example.com'
        }
        response = self.client.post(reverse('participant-list'), participant_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Participant.objects.count(), 2)
        self.assertEqual(Participant.objects.get(name='Jane Doe').email, 'jane@example.com')

    def test_create_registration(self):
        event = Event.objects.create(name='Django Meetup', date='2024-09-16', organizer=self.user)

        self.registration_data['event'] = event.id
        response = self.client.post(reverse('registration-list'), self.registration_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Registration.objects.count(), 1)
        self.assertEqual(Registration.objects.get().participant, self.participant)

    def test_event_list(self):
        Event.objects.create(name='Test Event', date='2024-09-20', organizer=self.user)
        response = self.client.get(reverse('event-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 1)

    def test_participant_list(self):
        response = self.client.get(reverse('participant-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)  # Initially 1 participant created in setUp

    def test_registration_list(self):
        event = Event.objects.create(name='Django Meetup', date='2024-09-16', organizer=self.user)
        Registration.objects.create(event=event, participant=self.participant)
        response = self.client.get(reverse('registration-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 1)

    def test_event_with_participants(self):
        event = Event.objects.create(name='Django Workshop', date='2024-09-17', organizer=self.user)
        event.participants.add(self.participant)

        response = self.client.get(reverse('event-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results'][0]['participants']), 1)
        self.assertEqual(response.data['results'][0]['participants'][0]['email'], 'john@example.com')

