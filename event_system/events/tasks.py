from celery import shared_task
from django.core.mail import send_mail
from django.http import HttpResponse
from django.apps import apps


@shared_task
def process_long_running_task(registration_id):
    # Process task completion
    # Example: sending a notification email
    print('111111')
    Registration = apps.get_model('events', 'Registration')
    registration = Registration.objects.get(id=registration_id)
    '''send_mail(
        'Registration Complete',
        f'Thank you for registering for {registration.event.name}',
        'no-reply@gamil.com',
        [registration.email],
        fail_silently=False,
    )'''
    return HttpResponse('Registration successful')
