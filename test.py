import os
import time
from Crypto.Cipher import AES

def aes_encrypt(plaintext, key, mode, iv=None):
    if mode == 'ECB':
        cipher = AES.new(key, AES.MODE_ECB)
    else:
        cipher = AES.new(key, getattr(AES, f"MODE_{mode}"), iv)
    return cipher.encrypt(plaintext)

def aes_decrypt(ciphertext, key, mode, iv=None):
    if mode == 'ECB':
        cipher = AES.new(key, AES.MODE_ECB)
    else:
        cipher = AES.new(key, getattr(AES, f"MODE_{mode}"), iv)
    return cipher.decrypt(ciphertext)

def test_performance():
    key = os.urandom(16)  # Generate a random key
    iv = os.urandom(16)   # Generate a random IV for modes that need it
    data = os.urandom(5 * 1024 * 1024)  # Generate 5MB of random data
    modes = ['ECB', 'CBC', 'CFB', 'OFB']
    
    print("Testing AES encryption and decryption speeds for different modes with 5MB of data:")
    for mode in modes:
        start_time = time.time()
        
        for _ in range(20):
            encrypted = aes_encrypt(data, key, mode, iv if mode != 'ECB' else None)
            decrypted = aes_decrypt(encrypted, key, mode, iv if mode != 'ECB' else None)
        
        end_time = time.time()
        total_time = (end_time - start_time) * 1000  # Convert time to milliseconds
        speed = (5 * 20 / (end_time - start_time))  # Calculate speed in MByte/sec

        print(f"{mode} mode - Total time for 20 iterations: {total_time:.2f} ms")
        print(f"{mode} mode - Speed: {speed:.2f} MByte/sec")

if __name__ == "__main__":
    test_performance()
