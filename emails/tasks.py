from celery import shared_task
from django.core.mail import send_mail
import csv

# @shared_task
# def send_bulk_emails(email_subject, email_message, email_from, recipient_list):
#     for recipient in recipient_list:
#         send_mail(
#             email_subject,
#             email_message,
#             email_from,
#             [recipient],
#             fail_silently=False,
#         )
#     return 'Emails Sent Successfully!'

@shared_task
def send_bulk_emails(email_subject, email_message, email_from, recipient_list):
    for recipient in recipient_list:
        send_mail(
            email_subject,
            email_message,
            email_from,
            [recipient],
            fail_silently=False,
        )
    return 'Emails Sent Successfully!'