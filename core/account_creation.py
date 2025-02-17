import random
import time

import requests

from core.constants import EULER_NUMBER, SINGUP_URL, STANDARD_HEADER


def get_session_and_csrf_token() -> tuple[requests.Session, str]:
    """
    Get a session and a CSRF token from Instagram signing page.
    """
    session = requests.Session()
    response = session.get(SINGUP_URL, headers=STANDARD_HEADER)
    csrf_token = response.cookies.get_dict()["csrftoken"]
    # time.sleep(EULER_NUMBER * 0.2) # TODO: this was intentional to take some time and don't make request very quick
    return session, csrf_token


form_data = {
    "email": "visabef623@perceint.com",
    "first_name": "Vis Abef",
    "username": "visabef",
}
