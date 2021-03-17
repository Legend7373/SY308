# !/usr/bin/env python3 
'''
Name: MIDN Austin D Andres  m220156
Section:  SY308 - 4001
Description: Lab1/HW5
Usage: 
'''
# Imported libraries
from sys import argv
import sys
from CBC import gen

if __name__ == "__main__":
    if len(argv) < 2:
        exit()
    gen((argv[1]))