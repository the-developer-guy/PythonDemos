from mymath.fake_crypto import encrypt

user_text = input("Please provide a text to encrypt: ")
encrypted_text = encrypt(user_text)

print(f"The 'encrypted' text is: {encrypted_text}")
