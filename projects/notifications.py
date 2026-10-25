import threading
from django.conf import settings
from utils import send_async_email


def notify_admin_of_project_request(name, email, message):
    email_body = f"""Hi Peter,

A new project request was submitted through your portfolio website, review details below.

Name: {name}
Email: {email}
Message: {message}
"""
    threading.Thread(
        target=send_async_email,
        args=(
            "New Project Request",
            email_body,
            settings.DEFAULT_FROM_EMAIL,
            ["peteroyelegbin@gmail.com"],
        ),
    ).start()
