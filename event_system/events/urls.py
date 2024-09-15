from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token
from .views import EventListView, ParticipantViewSet, RegistrationView, create_registration

router = DefaultRouter()
router.register(r'participants', ParticipantViewSet)


urlpatterns = [
    # Event List View URL
    path('', EventListView.as_view(), name='event-list-create'),

    # Registration View URL
    path('registrations/', RegistrationView.as_view(), name='registration-list-create'),

    # Custom registration creation view URL
    path('create-registration/', create_registration, name='create-registration'),

    # Include routes from the router for ParticipantViewSet
    path('', include(router.urls)),
]
