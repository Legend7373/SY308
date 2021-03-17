# !/usr/bin/env python3
'''
Name: MIDN Austin D Andres  m220156
Section:  SY308 - 4001
Description: HW4 problem 5
Usage: 
'''
# Imported libraries
from sys import argv
import sys
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
def openFs(key_file, cipher_bin, outF):
    with open(key_file, "rb") as key_f:
        key = b""
        key = key_f.read()
    with open(cipher_bin, "rb") as message_f:
        cipher_read = message_f.read()
    aes = AES.new(key, AES.MODE_ECB)
    new_key = (aes.encrypt(cipher_read[16:]))
    plaintxt = bytearray(16)
    for i in range(16):   
        plaintxt[i] = (cipher_read[i] ^ new_key[i])
    dec = open(outF, 'wb')
    dec.write(plaintxt)
    dec.close()
    return 
if __name__ == "__main__":
    if len(argv) < 4:
        exit()
    key_file = argv[1]
    cipher_bin = argv[2]
    outF = argv[3]
    openFs(key_file, cipher_bin, outF)