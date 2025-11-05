def caesar_cipher_encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            encrypted_text += chr((ord(char) - base + shift) % 26 + base)
        else:
            encrypted_text += char
    return encrypted_text

def caesar_cipher_decrypt(text, shift):
    return caesar_cipher_encrypt(text, -shift)

def main():
    print("Caesar Cipher Program")
    choice = input("Type 'encrypt' to encrypt or 'decrypt' to decrypt: ").strip().lower()
    message = input("Enter your message: ")
    try:
        shift = int(input("Enter shift value (integer): "))
    except ValueError:
        print("Invalid shift value. Please enter an integer.")
        return

    if choice == 'encrypt':
        result = caesar_cipher_encrypt(message, shift)
        print("Encrypted message:", result)
    elif choice == 'decrypt':
        result = caesar_cipher_decrypt(message, shift)
        print("Decrypted message:", result)
    else:
        print("Invalid choice. Please type 'encrypt' or 'decrypt'.")

if __name__ == "__main__":
    main()
