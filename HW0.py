# !/usr/bin/env python3 
'''
Name: MIDN Austin D Andres  m220156
Section:  SY308 - 4001
Description: 
Usage: 
'''
# Imported libraries

import random 
# Globals


def Problem4(a,b,n):
    array = []
    if n == 0:
        exit("Error")
    for i in range(0,10000):
        try:
            rand_num = random.randrange(a,b + 1)
            array.append(rand_num % n)
        except TypeError:
            exit()
    for num in range(a,b+1):
        percent = (array.count(num) / 10000) * 100
        answer = "Number " + str(num) + " : " + str(percent) + " %"
        print(answer) 
    return


