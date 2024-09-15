from django.shortcuts import render
from rest_framework import mixins, generics, viewsets
from .models import Registration, Event, Participant
from rest_framework.permissions import IsAuthenticated
from .serializers import RegistrationSerializer, ParticipantSerializer, EventSerializer
from rest_framework.pagination import PageNumberPagination
from django.db.models import Q

from django.db.models.signals import post_save
from django.dispatch import receiver
from .tasks import process_long_running_task
import threading
import time



class StandardResultsSetPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100

# Event List View with select_related and prefetch_related
class EventListView(generics.ListCreateAPIView):
    serializer_class = EventSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = StandardResultsSetPagination
    filterset_fields = ['name', 'date', 'organizer__email']

    def get_queryset(self):
        queryset = Event.objects.all()

        # Manual filtering
        name = self.request.query_params.get('name', None)
        date = self.request.query_params.get('date', None)
        organizer_email = self.request.query_params.get('organizer_email', None)

        if name:
            queryset = queryset.filter(name__icontains=name)
        if date:
            queryset = queryset.filter(date=date)
        if organizer_email:
            queryset = queryset.filter(organizer__email__icontains=organizer_email)
        
        return queryset

# Registration View using Mixins for CRUD
class RegistrationView(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.DestroyModelMixin,
    generics.GenericAPIView
):
    queryset = Registration.objects.all()
    serializer_class = RegistrationSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = StandardResultsSetPagination

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class ParticipantViewSet(viewsets.ModelViewSet):
    queryset = Participant.objects.all()
    serializer_class = ParticipantSerializer


def registration_task(instance_id):
    # Simulate a long-running task
    time.sleep(10)
    print(f"Long running task completed for registration ID: {instance_id}")

def create_registration(request):
    if request.method == 'POST':
        # Assume 'event_id' and 'participant_id' are provided in the POST data
        event_id = request.POST.get('event_id')
        participant_id = request.POST.get('participant_id')

        registration = Registration(event_id=event_id, participant_id=participant_id)
        registration.save()  # This saves the Registration instance to the database

        # Start the long-running task in a new thread
        threading.Thread(target=registration_task, args=(registration.id,)).start()