'''
Name: MIDN Austin D Andres  m220156
Section:  SY308 - 4001
Description: Lab1/HW5
Usage: 
'''
# Imported libraries
from sys import argv
import sys
from CBC import decrypt

def OpenAndWrite(key_file, cipherFile, outF):
    with open(key_file, "rb") as key_f:
        key = key_f.read()
    with open(cipherFile, "rb") as cipher:
        c = cipher.read().strip()
    plaintext = (decrypt(key, c)).decode()
    plaintext+="\n"
    dec = open(outF, 'w')
    dec.write(plaintext)
    dec.close()
   # print(plaintext)
if __name__ == "__main__":
    if len(argv) < 4:
        exit()
    key_file = argv[1]
    cipherFile = argv[2]
    outF = argv[3]
    OpenAndWrite(key_file, cipherFile, outF)