import requests
import time
from core.constants import STANDARD_HEADER, EULER_NUMBER, SINGUP_URL
import random


def get_session_and_csrf_token() -> tuple[requests.Session, str]:
    """
    Get a session and a CSRF token from Instagram signing page.
    """
    session = requests.Session()
    response = session.get(SINGUP_URL, headers=session.headers)
    csrf_token = response.cookies.get_dict()["csrftoken"]
    time.sleep(EULER_NUMBER * 0.2)
    return session, csrf_token


form_data = {
    "email": "visabef623@perceint.com",
    "first_name": "Vis Abef",
    "username": "visabef",
}
