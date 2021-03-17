# !/usr/bin/env python3 
'''
Name: MIDN Austin D Andres  m220156
Section:  SY308 - 4001
Description: HW0 problem 2
Usage: 
'''
# Imported libraries
from sys import argv
import random 
# Globals

def main():
    '''
    Description: Problem 2
    '''
    chars=[]
    filename = argv[1]
    try:
        with open(filename,'r') as f:
            lines = f.readlines()
    except:
        print('Error')
        exit()
    for i in lines:
        current_line = i.split()
        if len(current_line) == 1:
            current=current_line[0].split()
            if len(current[0]) == 5 :
                for l in current[0]:
                   chars.append(l)
                if chars[0] == 'S' and chars[1]== 'Y' and chars[2].isnumeric() and chars[3].isnumeric() and chars[4].isnumeric():
                    print(current[0])
        else:
            continue
    return
if __name__ == '__main__':
    main()