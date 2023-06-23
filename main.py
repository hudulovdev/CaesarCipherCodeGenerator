def caesar_cipher(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            if char.isupper():
                # Convert uppercase letter to ASCII code
                ascii_offset = ord('A')
            else:
                # Convert lowercase letter to ASCII code
                ascii_offset = ord('a')

            # Apply the shift and handle wrapping around the alphabet
            shifted_char = chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)
            result += shifted_char
        else:
            # Non-alphabetic characters are left unchanged
            result += char

    return result

# Example usage
plaintext = input("Enter text")
shift = input("Enter number: ")
ciphertext = caesar_cipher(plaintext, shift)
print("Ciphertext:", ciphertext)
