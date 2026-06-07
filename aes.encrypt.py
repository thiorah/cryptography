from cryptography.fernet import Fernet

# Generate AES key
key = Fernet.generate_key()

# Create cipher
cipher = Fernet(key)

# User input
message = input("Enter message: ")

# Encrypt message
encrypted = cipher.encrypt(message.encode())

print("\nEncrypted Message:")
print(encrypted)

# Decrypt message
decrypted = cipher.decrypt(encrypted)

print("\nDecrypted Message:")
print(decrypted.decode())