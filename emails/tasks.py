from celery import shared_task
from django.core.mail import EmailMultiAlternatives
import logging

# Set up logger
logger = logging.getLogger(__name__)

@shared_task
def send_bulk_emails(email_subject, email_message, email_from, recipient_list):
    for recipient in recipient_list:
        try:
            msg = EmailMultiAlternatives(
                email_subject,       
                '',                   
                email_from,          
                [recipient]          
            )
            msg.attach_alternative(email_message, "text/html")
            msg.send()
            logger.info(f"Email sent successfully to {recipient}")
            print(f"Email sent successfully to {recipient}")
        
        except Exception as e:
            logger.error(f"Failed to send email to {recipient}: {e}")
            print(f"Failed to send email to {recipient}: {e}")
    
    return 'Emails Sent Successfully!'