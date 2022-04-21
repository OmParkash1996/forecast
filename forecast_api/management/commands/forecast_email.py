import sys
from django.core.management.base import BaseCommand
from email.mime.text import MIMEText
import smtplib
from django.conf import settings
from datetime import datetime,timedelta
from forecast_api.models import Forecast
from django.utils import timezone

class Command(BaseCommand):

    def send_email(self,email_html, start_time, requested_by, body_message):
            subject = ' '.join(
                sys.argv[1:])

            MAIL_FROM = settings.EMAIL_HOST_USER
            MAIL_HOST = settings.EMAIL_HOST
            MAIL_PORT = settings.EMAIL_PORT
            MAIL_USER = settings.EMAIL_HOST_USER
            MAIL_PASS = settings.EMAIL_HOST_PASSWORD

            message = MIMEText(email_html, 'html')
            message['From'] = MAIL_FROM
            message = 'Subject: {}\n\n{}'.format("Forecasting History | " + str(start_time.strftime('%d-%m-%Y')),body_message)
            server = smtplib.SMTP('{0}:{1}'.format(MAIL_HOST, MAIL_PORT))
            server.starttls()
            server.login(MAIL_USER, MAIL_PASS)
            server.sendmail(MAIL_FROM, requested_by, message)
            server.quit()

    def handle(self, *args, **options):
        current_time = timezone.now()
        yesterday_date = current_time - timedelta(days = 1)
        users = Forecast.objects.all().values_list('user_id','user_id__email').distinct()
        for each_user in users:
            forecast_history = Forecast.objects.filter(user=each_user[0],requested_on__date=yesterday_date,is_emailed=False).values()
            if forecast_history:
                self.send_email("Forecasting Response", datetime.now(), each_user[1], forecast_history)
                forecast_history.update(is_emailed=True)