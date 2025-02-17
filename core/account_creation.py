import random
import time
from typing import Any
from urllib import response

import requests

from core.constants import EULER_NUMBER, SINGUP_URL
from core.utils import get_standard_header


def get_session_and_csrf_token() -> tuple[requests.Session, str]:
    """
    Get a session and a CSRF token from Instagram signing page.
    """
    session = requests.Session()
    response = session.get(SINGUP_URL, headers=get_standard_header())
    csrf_token = response.cookies.get_dict()["csrftoken"]
    # time.sleep(EULER_NUMBER * 0.2) # TODO: this was intentional to take some time and don't make request very quick
    return session, csrf_token, response


def perform_account_creation(
    email: str, password: str, first_name: str = None, username: str = None
) -> Any:  # TODO: the return is not clear for me either X.X
    session, csrf_token, response = get_session_and_csrf_token()

    headers = get_standard_header(session.headers)
    cookies = {
        "csrf_token": csrf_token,
    }

    form_data = {
        "email": email,
        "first_name": first_name,
        "username": username,
    }
