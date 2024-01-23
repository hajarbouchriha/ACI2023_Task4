# -*- coding: utf-8 -*-
"""
Created on Wed Jan 24 00:53:45 2024

@author: bouch
"""

from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.serialization import load_pem_private_key, load_pem_public_key
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
import base64
import os

# Symmetric Encryption (AES)
def aes_encrypt(key, data):
    cipher = Cipher(algorithms.AES(key), modes.CFB, backend=default_backend())
    encryptor = cipher.encryptor()
    cipher_text = encryptor.update(data) + encryptor.finalize()
    return cipher_text

def aes_decrypt(key, cipher_text):
    cipher = Cipher(algorithms.AES(key), modes.CFB, backend=default_backend())
    decryptor = cipher.decryptor()
    decrypted_data = decryptor.update(cipher_text) + decryptor.finalize()
    return decrypted_data

# Asymmetric Encryption (RSA)
def rsa_encrypt(public_key, data):
    encrypted_data = public_key.encrypt(
        data,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    return encrypted_data

def rsa_decrypt(private_key, encrypted_data):
    decrypted_data = private_key.decrypt(
        encrypted_data,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    return decrypted_data

# Key Generation
def generate_aes_key():
    return base64.urlsafe_b64encode(os.urandom(32))

def generate_rsa_key_pair():
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048,
        backend=default_backend()
    )
    public_key = private_key.public_key()
    return private_key, public_key

# Document the Implementation Process
def document_implementation():
    implementation_document = """
    **Encryption Implementation Documentation:**

    **Symmetric Encryption (AES):**
    - Algorithm: Advanced Encryption Standard (AES)
    - Key Size: 256 bits
    - Mode: Cipher Feedback (CFB)

    **Asymmetric Encryption (RSA):**
    - Algorithm: Rivest–Shamir–Adleman (RSA)
    - Key Size: 2048 bits
    - Padding: Optimal Asymmetric Encryption Padding (OAEP)

    **Key Generation:**
    - AES Key: 256-bit key generated using a secure random number generator.
    - RSA Key Pair: 2048-bit private key and corresponding public key.

    **Encryption/Decryption Process:**
    1. For symmetric encryption (AES), use AES key to encrypt and decrypt data.
    2. For asymmetric encryption (RSA), use RSA key pair to encrypt and decrypt data.

    **Key Management:**
    - Rotate AES keys every 6 months.
    - Rotate RSA key pairs every 12 months.

    **Integration:**
    - Integrate AES for data at rest encryption.
    - Integrate RSA for secure key exchange and communication.

    **Security Measures:**
    - Use secure random number generators for key generation.
    - Implement key rotation policies for increased security.

    **Ongoing Management Guidelines:**
    - Key Rotation: Rotate keys at specified intervals.
    - Incident Response: Define procedures for handling key compromises.
    - Audits: Regularly audit the encryption implementation.

    **Note:**
    - This documentation provides an overview of the encryption strategy and implementation.
    """
    print(implementation_document)

# Provide Guidelines for Ongoing Management
def ongoing_management_guidelines():
    ongoing_management = """
    **Ongoing Management Guidelines:**

    **Key Rotation Policy:**
    - Symmetric (AES): Rotate every 6 months.
    - Asymmetric (RSA): Rotate key pairs every 12 months.

    **Incident Response:**
    - Define procedures for handling key compromises.
    - Immediately rotate compromised keys.

    **Regular Audits:**
    - Conduct regular audits of the encryption implementation.
    - Verify compliance with key rotation policies.

    **Documentation Updates:**
    - Keep documentation up-to-date with any changes in the encryption strategy or key management practices.

    **Training and Awareness:**
    - Provide ongoing training for personnel involved in key management to ensure they understand and follow best practices.

    **Note:**
    - Ongoing management is crucial for maintaining the security and effectiveness of the encryption implementation.
    """
    print(ongoing_management)

# Example usage:
if __name__ == "__main__":
    # Generate keys
    aes_key = generate_aes_key()
    rsa_private_key, rsa_public_key = generate_rsa_key_pair()

    # Document the implementation
    document_implementation()

    # Provide ongoing management guidelines
    ongoing_management_guidelines()
