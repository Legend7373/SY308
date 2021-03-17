
if __name__ == "__main__":
    tfile = open('T2.bin', 'rb')
    ogT = tfile.readlines()
    tfile.close()
    t1=ogT[0]
    t2=ogT[1]
    ogT = t1 +t2
    message= open('M.txt', 'rb')
    m = message.readline().strip()
    message.close()
    m1 = m[:16]
    newM = bytearray(64)
    newM[:32] = m
    tf = bytearray(16)
    binM = open('Mforge2.bin', 'wb')
    for i in range(16):
        newM[i+32] = m1[i] ^ ogT[i]
    newM[48:] = m[16:]
    binM.write(newM)
    binM.close()
    tfile = open('Tforge2.bin', 'wb' )
    tfile.write(ogT)
    tfile.close()
    
