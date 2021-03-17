import MAC

def test():
    m = open("usna.bmp", "rb").read()
    t = bytes.fromhex("a73dbb7c009c4a86d4535940f7623c1a5a2e1d2a78c6dee31728ae43a8e6a66d") 
    k = bytes.fromhex("00112233445566778899aabbccddeeff")
    
    #============================================================
    # Checking mac
    #============================================================
    print("Checking mac function ...")
    if MAC.mac(k, m) != t:
        print("error: mac function is not correctly implemented")
        return
   
    print("Checking ver function ...")
    if MAC.ver(k, m, t)!= True:
        print("error: mac function is not correctly implemented")
        return
   
    print("Good!") 
    

test()
