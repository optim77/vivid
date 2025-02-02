import re

EMAIL_FORMAT = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'

def is_email(email):
    return re.match(EMAIL_FORMAT, email)