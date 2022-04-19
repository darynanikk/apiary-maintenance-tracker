from itsdangerous import URLSafeTimedSerializer
from itsdangerous.exc import BadSignature, BadData
from apiary_maintenance_service import settings
from django.core.mail import EmailMessage


class Util:
    @classmethod
    def send_email(cls, data):
        # TODO
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

    @classmethod
    def generate_confirmation_token(cls, email, user_id):
        secret_key = settings.SECRET_KEY
        secret_password_salt = settings.SECURITY_PASSWORD_SALT
        serializer = URLSafeTimedSerializer(secret_key)
        token = serializer.dumps({'email': email}, salt=secret_password_salt)
        return token

    @classmethod
    def confirm_token(cls, token, expiration=3600):
        serializer = URLSafeTimedSerializer(settings.SECURITY_PASSWORD_SALT)
        try:
            payload = serializer.loads(
                token,
                salt=settings.SECURITY_PASSWORD_SALT,
                max_age=expiration
            )
        except BadSignature as e:
            if e.payload is not None:
                try:
                    # This payload is decoded but unsafe because someone
                    # tampered with the signature.
                    return serializer.load_payload(e.payload)['email']
                except BadData:
                    return False
            else:
                return False
        else:
            return payload['email']
