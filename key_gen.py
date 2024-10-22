from cryptography.fernet import Fernet

key = Fernet.generate_key()
print(f"Nyckel: {key}")

with open("secret.key", "wb") as key_file:
    key_file.write(key)
print("Nyckeln har sparats som secret.key")
