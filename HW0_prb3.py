# !/usr/bin/env python3 
'''
Name: MIDN Austin D Andres  m220156
Section:  SY308 - 4001
Description: HW0 problem 3
Usage: 
'''
# Imported libraries

# Globals

def Problem3(array):
    pos_joint = ""
    for i in range(0, len(array)):
        current = array[i]
        if current.endswith('-'):
            pos_joint = current.strip('-')
        elif current.startswith('-') and pos_joint != "":
            answer = pos_joint + current.strip('-')
            print(answer)
            pos_joint=""
        else:
            pos_joint=""
            continue
    return

