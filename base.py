def encrypt(plaintext, shift):
    """Encrypts the plaintext using Caesar cipher with a given shift."""
    encrypted_text = []
    
    for char in plaintext:
        if char.isalpha():
            # Determine the ASCII offset for uppercase and lowercase letters
            offset = ord('A') if char.isupper() else ord('a')
            # Shift character and wrap around the alphabet
            shifted_char = chr((ord(char) - offset + shift) % 26 + offset)
            encrypted_text.append(shifted_char)
        else:
            # Non-alphabetic characters remain the same
            encrypted_text.append(char)
    
    return ''.join(encrypted_text)

def decrypt(ciphertext, shift):
    """Decrypts the ciphertext using Caesar cipher with a given shift."""
    decrypted_text = []
    
    for char in ciphertext:
        if char.isalpha():
            # Determine the ASCII offset for uppercase and lowercase letters
            offset = ord('A') if char.isupper() else ord('a')
            # Reverse shift character and wrap around the alphabet
            shifted_char = chr((ord(char) - offset - shift) % 26 + offset)
            decrypted_text.append(shifted_char)
        else:
            # Non-alphabetic characters remain the same
            decrypted_text.append(char)
    
    return ''.join(decrypted_text)


text = "Hello, World!"
shift = 3

encrypted = encrypt(text, shift)
print(f"Encrypted: {encrypted}")

decrypted = decrypt(encrypted, shift)
print(f"Decrypted: {decrypted}")
