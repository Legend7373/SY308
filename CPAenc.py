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
from os import urandom 
import os
def encrypt(key_file, message_file, outF):
    with open(key_file, "rb") as key_f:
        key = b""
        key = key_f.read()
    with open(message_file, "rb") as message_f:
        message = message_f.read()
    aes = AES.new(key, AES.MODE_ECB)
    IV = os.urandom(16)
    new_key = aes.encrypt(IV)
    ciphertext = bytearray(len(message))
    for i in range(len(message)):   
        ciphertext[i] = (new_key[i] ^ message[i])
    ciphertext+= IV
    enc = open(outF, 'wb')
    enc.write(ciphertext)
    enc.close()
if __name__ == "__main__":
    if len(argv) < 4:
        exit()
    key_file = argv[1]
    message_file = argv[2]
    outF = argv[3]
    encrypt(key_file, message_file, outF)
