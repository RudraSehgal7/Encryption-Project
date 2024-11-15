from Crypto.Random import get_random_bytes

def generate_aes_key():
    """
    Generates a random 256-bit AES key (32 bytes).
    
    Returns:
    - The generated AES key
    """
    return get_random_bytes(32)
