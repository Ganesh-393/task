import secrets, string
def random_password(length=10):
    chars = string.ascii_letters + string.digits + string.punctuation
    return ''.join(secrets.choice(chars) for _ in range(length))

print(random_password())

