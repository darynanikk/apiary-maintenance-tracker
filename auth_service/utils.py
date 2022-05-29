from django.core.mail import EmailMessage


class Util:
    @classmethod
    def send_email(cls, data):
        subject = data['email_subject']
        receiver = data['to_email']
        message = data['email_body']
        msg = EmailMessage(
            subject=subject,
            body=message,
            from_email='daryna-admin@example.com',
            to=[receiver],
            reply_to=['daryna-admin@example.com'],
            headers={'Message-ID': 'foo'},
        )
        msg.send()
