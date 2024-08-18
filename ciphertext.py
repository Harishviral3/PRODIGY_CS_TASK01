def caesar_cipher(text, shift, mode):
    result = ""

    # Traverse the text character by character
    for char in text:
        if char.isalpha():  # Check if the character is a letter
            shift_amount = shift if mode == 'encrypt' else -shift
            ascii_offset = 65 if char.isupper() else 97

            # Perform the shift and wrap around the alphabet if necessary
            new_char = chr((ord(char) - ascii_offset + shift_amount) % 26 + ascii_offset)
            result += new_char
        else:
            result += char  # Non-alphabetical characters remain unchanged

    return result

def main():
    # Get user inputs
    mode = input("Would you like to (e)ncrypt or (d)ecrypt?: ").strip().lower()
    message = input("Enter your message: ")
    shift = int(input("Enter the shift value: "))

    if mode == 'e':
        encrypted_message = caesar_cipher(message, shift, 'encrypt')
        print("Encrypted Message:", encrypted_message)
    elif mode == 'd':
        decrypted_message = caesar_cipher(message, shift, 'decrypt')
        print("Decrypted Message:", decrypted_message)
    else:
        print("Invalid mode selected. Please enter 'e' to encrypt or 'd' to decrypt.")

if __name__ == "__main__":
    main()
