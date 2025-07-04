from cryptography.fernet import Fernet

def generate_key():
    return Fernet.generate_key().decode()

def encrypt_message(key, message):
    f = Fernet(key.encode())
    return f.encrypt(message.encode()).decode()

def decrypt_message(key, token):
    f = Fernet(key.encode())
    return f.decrypt(token.encode()).decode()
