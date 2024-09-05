def encrypt(plaintext, shift):
    """Encrypts the plaintext using Caesar cipher with a given shift."""
    encrypted_text = []
    
    for char in plaintext:
        if char.isalpha():
          
            offset = ord('A') if char.isupper() else ord('a')
         
            shifted_char = chr((ord(char) - offset + shift) % 26 + offset)
            encrypted_text.append(shifted_char)
        else:
       
            encrypted_text.append(char)
    
    return ''.join(encrypted_text)

def decrypt(ciphertext, shift):
    """Decrypts the ciphertext using Caesar cipher with a given shift."""
    decrypted_text = []
    
    for char in ciphertext:
        if char.isalpha():
          
            offset = ord('A') if char.isupper() else ord('a')
           
            shifted_char = chr((ord(char) - offset - shift) % 26 + offset)
            decrypted_text.append(shifted_char)
        else:
          
            decrypted_text.append(char)
    
    return ''.join(decrypted_text)


text = "Hello, World!"
shift = 3

encrypted = encrypt(text, shift)
print(f"Encrypted: {encrypted}")

decrypted = decrypt(encrypted, shift)
print(f"Decrypted: {decrypted}")
