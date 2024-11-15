from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes

def encrypt_aes(plaintext, key):
    """
    Encrypt the plaintext using AES encryption algorithm
    Args:
    - plaintext: The text to be encrypted
    - key: The AES key (must be 16, 24, or 32 bytes long)
    
    Returns:
    - The encrypted text (in hexadecimal form)
    """
    cipher = AES.new(key, AES.MODE_CBC)
    ct_bytes = cipher.encrypt(pad(plaintext.encode(), AES.block_size))
    iv = cipher.iv
    encrypted_text = iv + ct_bytes
    return encrypted_text.hex()

def decrypt_aes(encrypted_text_hex, key):
    """
    Decrypt the encrypted text using AES decryption algorithm
    Args:
    - encrypted_text_hex: The encrypted text in hexadecimal form
    - key: The AES key
    
    Returns:
    - The decrypted plaintext
    """
    encrypted_text = bytes.fromhex(encrypted_text_hex)
    iv = encrypted_text[:16]  # Extract the IV
    ct_bytes = encrypted_text[16:]  # The ciphertext
    cipher = AES.new(key, AES.MODE_CBC, iv)
    decrypted_text = unpad(cipher.decrypt(ct_bytes), AES.block_size).decode()
    return decrypted_text
