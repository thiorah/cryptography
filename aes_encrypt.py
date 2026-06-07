from cryptography.fernet import Fernet

key = Fernet.generate_key()
cipher = Fernet(key)

message = input("Enter message: ")

encrypted = cipher.encrypt(message.encode())

print("Encrypted:", encrypted)

decrypted = cipher.decrypt(encrypted)

print("Decrypted:", decrypted.decode())
