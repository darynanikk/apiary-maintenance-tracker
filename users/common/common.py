import hashlib
import os
import random as r

PASSWORD = b"!@&?SECRET"
SALT = os.urandom(16)


def encode_random_password():
    password_hash = hashlib.pbkdf2_hmac("sha256", PASSWORD, SALT, 100000)
    password_hash = password_hash.hex()
    return password_hash


def generate_random_phone():
    formats = [
        "({}{}{}) {}{}{}-{}{}{}{}",
        "{}{}{}{}{}{}{}{}{}{}",
        "({}{}{})-{}{}{}-{}{}{}{}",
    ]

    ten_numbers = [r.randint(0, 9) for _ in range(10)]
    return r.choice(formats).format(*ten_numbers)



