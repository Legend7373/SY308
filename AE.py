import os
import CBC
import MAC
'''======================================================================
to do: choose a random pair of keys
    - one for CBC encryption (use CBC.gen)
    - one for HMAC (use MAC.mgen)
output: bytes type; 32 bytes
======================================================================'''
def gen():
    cbcKey = CBC.gen()
    hmackKey = CBC.gen()
    return cbcKey+hmackKey
'''======================================================================
to do: implement full AE encryption.
    0. split k into two keys (one for CBC, the other for HMAC)
    1. call CBC.encrypt and obtain ciphertext c
    2. call MAC.mac on c to obtain tag t 
    3. return the full ciphetext: c + t
input: 
    k: bytes type, must be 32 bytes 
    m: bytes type, any arbitrary-length message.  
output: 
    bytes type: ciphertext (CBC ciphertext + HMAC tag)
======================================================================'''
def encrypt(k, m):
    cbcKey = k[:16]
    hmacKey = k[16:]
    answer = bytes()
    c = CBC.encrypt(cbcKey, m)
    t = MAC.mac(hmacKey, c)
    return c+t
'''======================================================================
to do: implement full CBC decryption.
    0. split k into two keys (one for CBC, the other for HMAC)
    1. split c into two parts (c0: CBC-encryption, t: HMAC tag)
       The length of HMAC-SHA256 is 256 bits, that is, 32 bytes. 
    2. check if t is valid 
    3. if t is valid, do CBC.decrypt
input: 
    k: bytes type, must be 16 bytes
    c: bytes type, any arbitrary-length ciphertext.  
output: m, b
    m: bytes type
        return an empty bytes if an error occurs
======================================================================'''
def decrypt(k, c):
    cbcKey = k[:16]
    hmacKey = k[16:]
    c0 = c[:-32]
    answer = bytes()
    t = c[-32:]
    if MAC.ver(hmacKey, c0, t):
        answer = CBC.decrypt(cbcKey, c0)
    return answer



   

