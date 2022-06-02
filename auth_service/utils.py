from apiary_maintenance_service import settings
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail


class Util:
    @classmethod
    def send_email(cls, data):
        message = Mail(
            from_email='my.apiaryinfo@gmail.com',
            to_emails=data['to_email'],
            subject='Registration with Twilio Sendgrid',
            plain_text_content=data['email_body'])

        try:
            sg = SendGridAPIClient(settings.SENDGRID_API_KEY)
            response = sg.send(message)
            print(response.status_code)
            print(response.body)
            print(response.headers)
        except Exception as e:
            print(e)
