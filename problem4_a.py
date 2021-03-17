
if __name__ == "__main__":
    message= open('M.txt', 'rb')
    m = message.readline().strip()
    message.close()
    newM = bytearray(32)
    t = bytearray(16)
    for x in range(16,32):
        newM[x-16] = m[x] ^ 0
    for i in range(16):
        newM[i+16] = m[i] ^ 0
    binM = open('Mforge1.bin', 'wb')
    binM.write(newM)
    binM.close()
    tfile = open('T1.bin', 'rb')
    ogT = tfile.readline()
    for i in range(16):
        t[i] = ogT[i] ^ 0
    tfile.close()
    tfile = open('Tforge1.bin', 'wb' )
    tfile.write(t)
    tfile.close()