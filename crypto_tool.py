import argparse
from cryptography.fernet import Fernet


def load_key():
    with open("secret.key", "rb") as key_file:
        return key_file.read()


def encrypt_file(file_name):
    key = load_key()
    fernet = Fernet(key)

    
    with open(file_name, "rb") as file:
        file_data = file.read()

    
    encrypted_data = fernet.encrypt(file_data)

    
    with open(file_name + ".encrypted", "wb") as file:
        file.write(encrypted_data)

    print(f"Filen '{file_name}' har krypterats och sparats som '{file_name}.encrypted'.")


def decrypt_file(file_name):
    key = load_key()
    fernet = Fernet(key)

    
    with open(file_name, "rb") as file:
        encrypted_data = file.read()

    
    decrypted_data = fernet.decrypt(encrypted_data)

    
    original_file_name = file_name.replace(".encrypted", "")
    with open(original_file_name, "wb") as file:
        file.write(decrypted_data)

    print(f"Filen '{file_name}' har dekrypterats och sparats som '{original_file_name}'.")


def main():
    parser = argparse.ArgumentParser(description="Kryptera eller dekryptera en fil med en symmetrisk nyckel.")
    parser.add_argument("operation", choices=["encrypt", "decrypt"], help="Välj 'encrypt' för att kryptera en fil eller 'decrypt' för att dekryptera.")
    parser.add_argument("file", help="Filnamnet på den fil som ska krypteras eller dekrypteras.")
    
    args = parser.parse_args()

    if args.operation == "encrypt":
        encrypt_file(args.file)
    elif args.operation == "decrypt":
        decrypt_file(args.file)

if __name__ == "__main__":
    main()

