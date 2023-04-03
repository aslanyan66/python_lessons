import random
import string

def generate_emails(count, valid_format):
    emails = []
    for i in range(count):
        if valid_format:
            # Generate a valid email address
            username = ''.join(random.choices(string.ascii_lowercase + string.digits, k=10))
            domain = ''.join(random.choices(string.ascii_lowercase, k=5))
            extension = random.choice(['com', 'net', 'org', 'edu'])
            email = f"{username}@{domain}.{extension}"
        else:
            # Generate an invalid email address
            email = ''.join(random.choices(string.ascii_lowercase + string.digits + '-_@.', k=20))
        emails.append(email)
    return emails