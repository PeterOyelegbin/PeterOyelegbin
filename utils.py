from django.core.mail import EmailMultiAlternatives
import hashlib


# Avatar generation from mail
def get_gravatar_url(email, size=100):
    email_hash = hashlib.md5(email.strip().lower().encode('utf-8')).hexdigest()
    return f"https://www.gravatar.com/avatar/{email_hash}?s={size}&d=identicon"


# Asynchronous email sending
def send_async_email(subject, message, from_email, recipient_list):
    try:
        email = EmailMultiAlternatives(subject, message, from_email, recipient_list)
        email.send()
    except Exception as e:
        print(f"Error sending email: {e}")