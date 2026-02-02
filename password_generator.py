import secrets
import string

def secret_generated_password(size: int = 53):
	characters = string.punctuation + string.ascii_letters + string.digits
	secret_password = ''.join(secrets.choice(characters) for _ in range(size))
	return secret_password

secret_password = secret_generated_password()
print(f"Your secret password is: {secret_password}")