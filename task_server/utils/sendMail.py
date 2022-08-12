from django.core.mail import send_mail
from django.conf import settings


def Mailer(subject, message, recipient_list):
    try:
        print(settings.EMAIL_HOST_USER)
        send_mail(subject, message, settings.EMAIL_HOST_USER, [recipient_list])
        return True
    except Exception as e:
        return str(e)
