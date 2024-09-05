Encryption Function (encrypt):

    For each character in the plaintext:
        If the character is an alphabet letter, shift it by the specified amount (shift).
        Handle both uppercase and lowercase letters.
        Wrap around the alphabet if necessary using modulo arithmetic.
        Non-alphabetic characters are not changed.

Decryption Function (decrypt):

    For each character in the ciphertext:
        If the character is an alphabet letter, reverse the shift by subtracting the specified amount.
        Handle both uppercase and lowercase letters.
        Wrap around the alphabet if necessary using modulo arithmetic.
        Non-alphabetic characters are not changed.