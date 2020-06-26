from celery.utils.log import get_task_logger

from periodic.app import app
from periodic.utils.xmodels import get_auth_profile_model
from project.utils.consts import PROJECT_NAME
from project.utils.safeguards import safe
from project.utils.xdatetime import utcnow
from project.utils.xmail import send_email

logger = get_task_logger(__name__)


@app.task
@safe
def invite_single_user(email: str):
    logger.debug(f"BEGIN | {invite_single_user.__name__} | {email}")

    auth_profile_model = get_auth_profile_model()
    auth_profile = auth_profile_model.objects.get(user__email=email)

    logger.debug(f"IN | {invite_single_user.__name__} | {auth_profile}")
    if not auth_profile.link:
        logger.debug(
            f"END |"
            f" {invite_single_user.__name__} |"
            f" skip {auth_profile}, reason: no link"
        )
        return

    service = PROJECT_NAME.capitalize()

    send_email(
        context={"link": auth_profile.link, "service": service},
        email_to=email,
        mail_template_name="invitation",
        subject=f"Registration at {service}",
    )

    auth_profile.notified_at = utcnow()
    auth_profile.save()

    logger.debug(
        f"END | {invite_single_user.__name__} | email for {auth_profile} has been sent"
    )
