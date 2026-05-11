import string
import secrets
import hashlib
import base64
from zxcvbn import zxcvbn

def get_password_report(password):
    if not password: return None
    return zxcvbn(password)

def generate_secure_password(length=16):
    alphabet = string.ascii_letters + string.digits + string.punctuation
    return ''.join(secrets.choice(alphabet) for i in range(length))

def encrypt_password(password, method="SHA-256"):
    if method == "SHA-256":
        return hashlib.sha256(password.encode()).hexdigest()
    elif method == "Base64":
        return base64.b64encode(password.encode()).decode()
    return password