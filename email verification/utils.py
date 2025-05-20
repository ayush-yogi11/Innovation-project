from django.core import signing

def generate_token(email):
    return signing.dumps(email)

def verify_token(token, max_age=3600):  # 1 hour expiry
    try:
        email = signing.loads(token, max_age=max_age)
        return email
    except signing.SignatureExpired:
        return None
    except signing.BadSignature:
        return None
