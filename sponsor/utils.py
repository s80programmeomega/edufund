from django.core.mail import send_mail
from django.conf import settings
from typing import Union
from .models import Donation, AnonymousDonation


def send_donation_notification(donation: Union[Donation, AnonymousDonation]):
    """
    Send email notifications about new donations
    """
    sponsor = donation.sponsor.name, donation.sponsor.email if hasattr(
        donation, 'sponsor') else f'Anonymous with email: {donation.email}'

    subject = 'New Donation Received'
    message = f'''
    We have successfully received your donnation
    
    Amount: {donation.amount}
    Campaign:{donation.funding_campaign.name}
    The funding progression is now: {donation.funding_campaign.funding_progression}
    sponsor: {sponsor}
    Date: {donation.date_added}
    
    Thank you for your support
    '''

    recipient_email_list = []

    if isinstance(donation, Donation):
        recipient_email = donation.sponsor.email
        sponsor_representatives_email = [
            representative.email for representative in donation.sponsor.representative.all()]

        sponsor_representatives_email.append(recipient_email)
        recipient_email_list = sponsor_representatives_email
    else:
        recipient_email_list = list(donation.email)

    # Sponsor notification
    send_mail(
        subject=subject,
        message=message,
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=recipient_email_list,
        fail_silently=False,
    )

    # Shool notification (if applicable)
    school_subject = 'New donation!'
    school_message = f'''
    Good news! You received a new donation:
    Campaign:{donation.funding_campaign.name} 
    Amount: {donation.amount}
    The funding progression is now: {donation.funding_campaign.funding_progression}
    Donor: {sponsor}
    Date: {donation.date_added}
    '''
    schools = donation.funding_campaign.schools.all()
    representatives = [
        representative for school in schools for representative in school.representatives.all()]
    school_email_list = [
        representative.email for representative in representatives]

    send_mail(
        subject=school_subject,
        message=school_message,
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=school_email_list,
        fail_silently=False,
    )
