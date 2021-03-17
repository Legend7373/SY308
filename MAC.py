import os
from Crypto.Hash import HMAC
from Crypto.Hash import SHA256
from CBC import gen


'''======================================================================
to do: choose a random key
output: bytes type; 16 bytes
======================================================================'''
def mgen():
    print(gen())
    return gen()
'''======================================================================
to do: implement MAC algorithm. 
    - Read the notes carefully. 
    - Use SHA256 for HMAC
input: 
    k: bytes type, must be 16 bytes
    d: bytes type, any arbitrary-length data
output: 
    bytes: mac tag
======================================================================'''
def mac(k, d): 
    h = SHA256.new()
    hmac = HMAC.new(k, digestmod=h)
    hmac.update(d)
    hmac.digest()
    #print(hmac.digest())
    return hmac.digest()
     

'''======================================================================
to do: implement MAC verification algorithm
    1. call mac(k, d)
    2. see if the output of mac(k,d) is the same as t
input: 
    k: bytes type, must be 16 bytes
    d: bytes type, any arbitrary-length data. 
    t: bytes type, must be 32 bytes 
output: b
    b: Boolean: True if success; False otherwise 
======================================================================'''
def ver(k, d, t):
    if mac(k, d) == t:
        return True
    return False
        
