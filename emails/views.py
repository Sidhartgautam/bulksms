from django.core.mail import get_connection, EmailMessage
from django.template.loader import render_to_string
from django.shortcuts import render
from .forms import EmailUploadForm
from .models import EmailLog
import csv
import logging
from emails.tasks import send_bulk_emails
from django.conf import settings

logger = logging.getLogger(__name__)

def upload_csv(request):
    if request.method == 'POST':
        form = EmailUploadForm(request.POST, request.FILES)
        if form.is_valid():
            csv_file = request.FILES['csv_file']
            email_list = []

            # Parse CSV file
            try:
                decoded_file = csv_file.read().decode('utf-8').splitlines()
                reader = csv.DictReader(decoded_file)
                email_column = 'email' 

                for row in reader:
                    email = row.get(email_column, '').strip()
                    if email:
                        email_list.append(email)
                    else:
                        logger.warning(f"Empty or missing email address found in row: {row}")

                logger.info(f"Emails extracted: {email_list}")
            except Exception as e:
                logger.error(f"Error reading CSV file: {e}")
                return render(request, 'upload_csv.html', {'form': form, 'error': 'Error reading CSV file'})
            subject = 'Öka era intäkter med More Channel!'
            from_email = settings.DEFAULT_FROM_EMAIL
            html_message = render_to_string('email_template.html', {
            })

            send_bulk_emails.delay(subject, html_message, from_email, email_list)

            return render(request, 'upload_success.html')
    else:
        form = EmailUploadForm()

    return render(request, 'upload_csv.html', {'form': form})
def homepage(request):
    return render(request, 'homepage.html')

