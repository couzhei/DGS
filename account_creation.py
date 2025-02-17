"""
Creates an Instagram account programmatically by simulating browser interactions.

This script uses Selenium WebDriver to automate the process of creating an Instagram account.
It fills in registration forms with provided user information and handles required actions
like accepting cookies and navigating through signup steps.

Parameters:
    USERNAME (str): Desired Instagram username for the new account
    PASSWORD (str): Password to set for the new account
    EMAIL (str): Email address to associate with the account
    FULL_NAME (str): Full name to use for the account
    GENDER (str): Gender selection for the account
    BIRTHDAY (str): Birthday to use for the account (format: yyyy-mm-dd)

Note:
    - May be subject to Instagram's anti-automation measures
    - Use responsibly and in accordance with Instagram's Terms of Service (seriously?)
    - Success not guaranteed due to potential changes in Instagram's signup process
"""

import random
import time

import requests

# Step 2: Prepare headers and body for the request
# You can easily get these using https://curlconverter.com/ (translates curl into Python codes)


cookies = {
    "csrftoken": "suzeB5HzQp9TPiYFsGcPMd",
}

headers = {
    "accept": "*/*",
    "accept-language": "en-US,en;q=0.9,fa;q=0.8",
    "content-type": "application/x-www-form-urlencoded",
    # 'cookie': 'csrftoken=suzeB5HzQp9TPiYFsGcPMd',
    "origin": "https://www.instagram.com",
    "priority": "u=1, i",
    "referer": "https://www.instagram.com/accounts/emailsignup/",
    "sec-ch-prefers-color-scheme": "dark",
    "sec-ch-ua": '"Not A(Brand";v="8", "Chromium";v="132", "Microsoft Edge";v="132"',
    "sec-ch-ua-full-version-list": '"Not A(Brand";v="8.0.0.0", "Chromium";v="132.0.6834.160", "Microsoft Edge";v="132.0.2957.140"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-model": '""',
    "sec-ch-ua-platform": '"Windows"',
    "sec-ch-ua-platform-version": '"19.0.0"',
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36 Edg/132.0.0.0",
    "x-asbd-id": "129477",
    "x-csrftoken": "suzeB5HzQp9TPiYFsGcPMd",
    "x-ig-app-id": "936619743392459",
    "x-ig-www-claim": "0",
    "x-instagram-ajax": "1019965497",
    "x-requested-with": "XMLHttpRequest",
    "x-web-device-id": "D0D53B30-92E0-4AB4-B2A6-618E6A022224",
    "x-web-session-id": "::l9ov59",
}


data = {
    "email": "ashkanmehravand@gmail.com",
    "failed_birthday_year_count": "{}",
    "first_name": "Ashkan Mehravand",
    "username": "ashkanmehr",
    "opt_into_one_tap": "false",
    "use_new_suggested_user_name": "true",
}

response = requests.post(
    "https://www.instagram.com/api/v1/web/accounts/web_create_ajax/attempt/",
    cookies=cookies,
    headers=headers,
    data=data,
)
print(response.json())

# This will output something like this
my_dict = {
    "account_created": False,
    "errors": {
        "username": [
            {
                "message": "This username isn't available. Please try another.",
                "code": "username_is_taken",
            }
        ],
        "__all__": [
            {
                "message": "Create a password at least 6 characters long.",
                "code": "too_short_password",
            }
        ],
    },
    "dryrun_passed": False,
    "username_suggestions": [
        "ashka_nmehr",
        "ashk_anmehr",
        "ashka.nmehr",
        "ash.kanmehr",
        "ash_kanmehr",
        "ashkanmehr2025",
        "ashkanmehr26",
        "ashkanmehr709",
        "ashkanmehr3455",
    ],
    "status": "ok",
    "error_type": "form_validation_error",
}


input()
# Get CSRF token (you might not be able to get it by directly requests.get() the page)
session = requests.Session()
response = session.get("https://www.instagram.com/accounts/emailsignup/")
csrf_token = session.cookies.get("csrftoken")


cookies = {
    "csrftoken": csrf_token,
}

headers = {
    "x-csrftoken": csrf_token,
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)...",
    "referer": "https://www.instagram.com/accounts/emailsignup/",
}
headers = {
    "accept": "*/*",
    "accept-language": "en-US,en;q=0.9,fa;q=0.8",
    "content-type": "application/x-www-form-urlencoded",
    # 'cookie': 'csrftoken=suzeB5HzQp9TPiYFsGcPMd',
    "origin": "https://www.instagram.com",
    "priority": "u=1, i",
    "referer": "https://www.instagram.com/accounts/emailsignup/",
    "sec-ch-prefers-color-scheme": "dark",
    "sec-ch-ua": '"Not A(Brand";v="8", "Chromium";v="132", "Microsoft Edge";v="132"',
    "sec-ch-ua-full-version-list": '"Not A(Brand";v="8.0.0.0", "Chromium";v="132.0.6834.160", "Microsoft Edge";v="132.0.2957.140"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-model": '""',
    "sec-ch-ua-platform": '"Windows"',
    "sec-ch-ua-platform-version": '"19.0.0"',
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36 Edg/132.0.0.0",
    "x-asbd-id": "129477",
    "x-csrftoken": csrf_token,
    "x-ig-app-id": "936619743392459",
    "x-ig-www-claim": "0",
    "x-instagram-ajax": "1019965497",
    "x-requested-with": "XMLHttpRequest",
    "x-web-device-id": "D0D53B30-92E0-4AB4-B2A6-618E6A022224",
    "x-web-session-id": "::l9ov59",
}
data = {
    "email": "student1@yourorg.com",
    "username": "student1_creative",
    "password": "SecurePass123!",
}

attempt_response = session.post(
    "https://www.instagram.com/api/v1/web/accounts/web_create_ajax/attempt/",
    headers=headers,
    data=data,
    cookies=cookies,
)
print(attempt_response.json())  # Check for errors
input()


# Step 3: Submit final request (if validation passes)
if attempt_response.json().get("dryrun_passed"):
    final_response = session.post(
        "https://www.instagram.com/api/v1/web/accounts/web_create_ajax/",
        headers=headers,
        data=data,
    )
    print(final_response.json())
else:
    print("Validation failed.")


# TODO:
# We might need to send a request to both chec
# https://www.instagram.com/api/v1/web/consent/check_age_eligibility/
# https://www.instagram.com/api/v1/accounts/send_verify_email/
# to make sure everything is intact!
