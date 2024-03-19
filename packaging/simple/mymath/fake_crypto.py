from .fake_random import random_die

def encrypt(text: str, key: int=random_die()) -> str:
    """Ooops, forgot to encrypt"""
    print(f"Encryption key: {key}")
    return text
