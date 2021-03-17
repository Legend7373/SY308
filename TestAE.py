import AE

def test():
    m = open("usna.bmp", "rb").read()
    k = bytes.fromhex("0123456789ABCDEFABCDEF01234567890123456789ABCDEFABCDEF0123456789")
    c0 = open("usna.bin", "rb").read()
    c1 = open("usna1.bin", "rb").read()
    c2 = open("usna2.bin", "rb").read()
    
    print("Checking AE.decrypt()...")
    if AE.decrypt(k,c0) != m:  
        print("error: decrypt is not implemented correctly")
        return
    if AE.decrypt(k,c1) != bytes():   
        print("error: decrypt is not implemented correctly")
        print("usna1.bin is an invalid ciphertext")
        return

    if AE.decrypt(k,c2) != bytes():   
        print("error: decrypt is not implemented correctly")
        print("usna2.bin is an invalid ciphertext")
        return


    print("Checking AE.encrypt()...") 
    c3 = AE.encrypt(k,m)
    c4 = AE.encrypt(k,m)
    if c3 == c4:
        print("error: encrypt is not randomized")   
        return

    if AE.decrypt(k,c3) != m:   
        print("error: decrypt is not implemented correctly")
        return
    
    if AE.decrypt(k,c4) != m:   
        print("error: decrypt is not implemented correctly")
        return
    print("Good!") 
    
test()
