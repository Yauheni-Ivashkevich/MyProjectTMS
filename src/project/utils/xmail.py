from typing import Dict
from typing import Optional

from django.conf import settings
from django.core.mail import send_mail
from django.http import HttpRequest
from django.template.loader import get_template

# from project.jinja2 import environment as env
from project.utils.safeguards import safe


@safe
def send_email(
    email_to: str,
    subject: str,
    mail_template_name: str,
    context: Optional[Dict] = None,
    request: Optional[HttpRequest] = None,
):  # pragma: no cover
    request = (
        request or HttpRequest()
    )  #'tmpl_d973d98d4ea845be2739a97d166f0523917d4523.py'
    template_txt = get_template(f"mail/txt/{mail_template_name}.txt")
    template_html = get_template(f"mail/html/{mail_template_name}.html")

    message_txt = template_txt.render(context, request)
    message_html = template_html.render(context, request)

    return send_mail(
        from_email=settings.EMAIL_FROM,
        html_message=message_html,
        message=message_txt,
        recipient_list=[email_to],
        subject=subject,
    )
