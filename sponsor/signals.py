from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Donation, AnonymousDonation
from .utils import send_donation_notification


@receiver(post_save, sender=Donation)
def donation_notification(sender, instance, created, **kwargs):
    if created:  # Only send notification for new donations
        print(
            f"===>A New Donation Was MAde: {Donation.__class__}<===")
        send_donation_notification(instance)


@receiver(post_save, sender=AnonymousDonation)
def donation_notification(sender, instance, created, **kwargs):
    if created:
        print(
            f"===>A New Donation Was MAde: {AnonymousDonation.__class__}<===")
        send_donation_notification(instance)
