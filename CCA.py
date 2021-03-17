import sys
from sys import argv
from Crypto.Random import get_random_bytes, new
from Crypto.Cipher import AES

if __name__ == "__main__":
    message= open('cbc.bin', 'rb')
    m = message.readline()
    message.close()
    ln = len(m)
    newM = bytearray(ln)
    for i in range(ln):
        if i == ln-19:
            newM[i] = m[i] ^ 1
        else: 
            newM[i] = m[i] ^ 0
    binM = open('Mforge1.bin', 'wb')
    binM.write(newM)
    binM.close()
    