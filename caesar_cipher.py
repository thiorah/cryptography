text = input("Enter message: ")
if text == "":
    print("Input cannot be empty")
else:
 shift = 3

encrypted = ""

for char in text:
    if char.isalpha():
        encrypted += chr((ord(char) - 65 + shift) % 26 + 65)
    else:
        encrypted += char

print("Encrypted:", encrypted)