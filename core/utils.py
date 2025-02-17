import base64
import binascii
import datetime
import json
import random
import re
import struct
from datetime import date

import requests
from Crypto import Random
from Crypto.Cipher import AES
from nacl.public import PublicKey, SealedBox

from core.constants import STANDARD_HEADERS


def get_standard_header(custom_header: dict = None) -> dict:
    """
    Returns the standard Instagram headers. Optionally merges with custom headers.

    Parameters:
        custom_headers (dict): A dictionary of custom headers to add or override.

    Returns:
        dict: The final headers for the request.
    """
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36",
        "Referer": "https://www.instagram.com/",
        "X-Requested-With": "XMLHttpRequest",
    }

    headers.update(STANDARD_HEADERS)

    if custom_header:
        custom_header.update(headers)

    return headers


def get_instagram_encryption_data(session: requests.Session, url=None) -> dict:
    """
    Fetches the Instagram encryption data from the signup page using the provided session.

    Args:
        session (requests.Session): A session object with any necessary headers already set.

    Returns:
        dict: A dictionary containing the encryption data. For example:
              {
                  "key_id": ...,
                  "public_key": ...,
                  "version": ...
              }

    Raises:
        ValueError: If the encryption data cannot be found in the page.
    """
    if not url:
        url = SINGUP_URL
    response = session.get(SINGUP_URL)
    html = response.text

    pattern = r'InstagramPasswordEncryption",\s*\[\s*\],\s*(\{.*?\}),'
    match = re.search(pattern, html)

    if match:
        encryption_data = json.loads(match.group(1))
        return encryption_data
    else:
        raise ValueError("Encryption data not found")


def encrypt_password(password, key_id, public_key, version):
    """
    Encrypts a given password using AES encryption and a public key.

    Args:
        key_id (int): Identifier for the encryption key.
        public_key (str): Public key used for encryption.
        version (int): Version of the encryption scheme.
        password (str): Password to be encrypted.

    Returns:
        str: Encrypted password string in the format `#PWD_INSTAGRAM_BROWSER:{version}:{time}:{encrypted}`.
    """
    key = Random.get_random_bytes(32)
    iv = bytes([0] * 12)

    time = int(datetime.datetime.now().timestamp())

    aes = AES.new(key, AES.MODE_GCM, nonce=iv, mac_len=16)
    aes.update(str(time).encode("utf-8"))
    encrypted_password, cipher_tag = aes.encrypt_and_digest(password.encode("utf-8"))

    pub_key_bytes = binascii.unhexlify(public_key)
    seal_box = SealedBox(PublicKey(pub_key_bytes))
    encrypted_key = seal_box.encrypt(key)

    encrypted = bytes(
        [
            1,
            int(key_id),
            *list(struct.pack("<h", len(encrypted_key))),
            *list(encrypted_key),
            *list(cipher_tag),
            *list(encrypted_password),
        ]
    )
    encrypted = base64.b64encode(encrypted).decode("utf-8")
    return f"#PWD_INSTAGRAM_BROWSER:{version}:{time}:{encrypted}"


def generate_random_birthdate() -> dict:
    """
    Generates a random birthdate ensuring the person is between 18 and 60 years old,
    as calculated from February 17, 2025. Returns a dictionary with keys 'day', 'month', and 'year'.

    Returns:
        dict: A dictionary containing a valid birthdate.
    """
    # Reference current date for eligibility (change if needed)
    current_date = date.today()

    # Calculate the earliest and latest eligible birthdates.
    # Person must be at most 60 years old and at least 18 years old.
    earliest = current_date.replace(year=current_date.year - 60)
    latest = current_date.replace(year=current_date.year - 18)

    # Convert dates to ordinal numbers (integers) and generate a random ordinal
    random_ordinal = random.randint(earliest.toordinal(), latest.toordinal())
    birth_date = date.fromordinal(random_ordinal)

    return {"day": birth_date.day, "month": birth_date.month, "year": birth_date.year}
