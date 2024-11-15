from encryption.aes_encryption import encrypt_aes, decrypt_aes
from utils.key_management import generate_aes_key

def main():
    print("Welcome to the AES Encryption App!")
    
    # Generate a new AES key
    key = generate_aes_key()
    
    # Input for text to be encrypted
    plaintext = input("Enter text to encrypt: ")
    
    # Encrypt the text
    encrypted_text = encrypt_aes(plaintext, key)
    print(f"Encrypted Text: {encrypted_text}")
    
    # Decrypt the text
    decrypted_text = decrypt_aes(encrypted_text, key)
    print(f"Decrypted Text: {decrypted_text}")
    
if __name__ == "__main__":
    main()
