from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Registration
import threading
import time

def registration_task(instance_id):
    # Simulate a long-running task
    time.sleep(10)
    print(f"Long running task completed for registration ID: {instance_id}")

@receiver(post_save, sender=Registration)
def handle_registration_post_save(sender, instance, **kwargs):
    print('YESSSSSSSSSSSSSSS')  # Debugging print statement
    # Start the long-running task in a new thread
    threading.Thread(target=registration_task, args=(instance.id,)).start()