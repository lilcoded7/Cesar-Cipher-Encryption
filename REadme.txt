Caesar Cipher

The Caesar cipher is one of the simplest and most well-known encryption techniques. Named after Julius Caesar, who reportedly used it to encode his messages, it is a type of substitution cipher where each letter in the plaintext is replaced by a letter some fixed number of positions down or up the alphabet.
How It Works

    Encryption: Each letter in the plaintext is shifted a fixed number of positions forward in the alphabet.
    Decryption: Each letter in the ciphertext is shifted backward by the same fixed number of positions to retrieve the original plaintext.

Encryption Function (encrypt)

This function performs the Caesar cipher encryption as follows:

    Input:
        plaintext (string): The text to be encrypted.
        shift (integer): The number of positions each letter in the plaintext will be shifted.

    Process:
        For each character in the plaintext:
            If the character is an alphabet letter:
                Shift it by the specified amount (shift).
                Handle both uppercase and lowercase letters.
                Use modulo arithmetic to wrap around the alphabet if the shift goes past 'Z' or 'z'.
            Non-alphabetic characters (e.g., spaces, punctuation) remain unchanged.

    Output:
        Returns the encrypted text as a string.

Decryption Function (decrypt)

This function performs the Caesar cipher decryption as follows:

    Input:
        ciphertext (string): The text to be decrypted.
        shift (integer): The number of positions each letter in the ciphertext will be shifted backward.

    Process:
        For each character in the ciphertext:
            If the character is an alphabet letter:
                Reverse the shift by subtracting the specified amount (shift).
                Handle both uppercase and lowercase letters.
                Use modulo arithmetic to wrap around the alphabet if the shift goes before 'A' or 'a'.
            Non-alphabetic characters (e.g., spaces, punctuation) remain unchanged.

    Output:
        Returns the decrypted text as a string.

text = "Hello, World!"
shift = 3

# Encrypt the plaintext
encrypted = encrypt(text, shift)
print(f"Encrypted: {encrypted}")

# Decrypt the ciphertext
decrypted = decrypt(encrypted, shift)
print(f"Decrypted: {decrypted}")


Encrypting "Hello, World!" with a shift of 3 results in "Khoor, Zruog!".
Decrypting "Khoor, Zruog!" with the same shift value returns the original text "Hello, World!".
