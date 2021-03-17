# !/usr/bin/env python3 
'''
Name: MIDN Austin D Andres  m220156
Section:  SY308 - 4001
Description: Lab1/HW5
Usage: 
'''
# Imported libraries
from sys import argv
import sys
from CBC import encrypt

def OpenAndWrite(key_file, message_file, outF):
    with open(key_file, "rb") as key_f:
        key = key_f.read()
    with open(message_file, "rb") as message_f:
        message = message_f.read().strip()
    ciphertext = encrypt(key, message)
    enc = open(outF, 'wb')
    enc.write(ciphertext)
    enc.close()
    #print(ciphertext)
if __name__ == "__main__":
    if len(argv) < 4:
        exit()
    key_file = argv[1]
    message_file = argv[2]
    outF = argv[3]
    OpenAndWrite(key_file, message_file, outF)