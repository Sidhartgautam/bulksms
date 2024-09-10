from celery import shared_task
from django.core.mail import send_mail
import csv
from django.core.mail import EmailMultiAlternatives



@shared_task
def send_bulk_emails(email_subject, email_message, email_from, recipient_list):
    for recipient in recipient_list:
        # Create the email message
        msg = EmailMultiAlternatives(
            email_subject,        # Subject
            '',                   # Plain text content (optional)
            email_from,           # From email
            [recipient]           # Recipient list
        )
        # Attach the HTML content
        msg.attach_alternative(email_message, "text/html")
        # Send the email
        msg.send()
    
    return 'Emails Sent Successfully!'