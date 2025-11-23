# Encrypt a message using Caesar Cipher
def encrypt(message, key): 
    result = ""

    for char in message:
        # Only shift letters
        if char.isalpha():
            shift = ord(char) + key

            # Wrap lowercase
            if char.islower() and shift > ord('z'):
                shift -= 26
            
            # Wrap uppercase
            if char.isupper() and shift > ord('Z'):
                shift -= 26

            result += chr(shift)
        else:
            result += char
    
    return result

# Decrypt by shifting in the opposite direction
def decrypt(message, key):
    return encrypt(message, -key)

# User input
msg = input("Enter message: ")
key = int(input("Enter key: "))

encrypted = encrypt(msg, key)
decrypted = decrypt(encrypted, key)

print("Encrypted:", encrypted)
print("Decrypted:", decrypted)
