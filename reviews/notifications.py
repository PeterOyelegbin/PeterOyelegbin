import threading
from django.conf import settings
from utils import send_async_email


def notify_admin_of_review_submission():
    threading.Thread(
        target=send_async_email,
        args=(
            "New Review Uploaded",
            """Hi Peter,

A new review has been submitted for approval on your portfolio website. Please log in to the admin panel to approve upon review.

Best regards,
https://peter.oyelegbin.name.ng/admin""",
            settings.DEFAULT_FROM_EMAIL,
            ["peteroyelegbin@gmail.com"],
        ),
    ).start()
