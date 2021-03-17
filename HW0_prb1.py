# !/usr/bin/env python3 
'''
Name: MIDN Austin D Andres  m220156
Section:  SY308 - 4001
Description: HW0 problem 1
Usage: 
'''
# Imported libraries

# Globals


def Problem1(array1, array2):
    answer=[]
    loop_size = max(len(array1), len(array2))
    for i in range(0,loop_size):
        try:
            answer.append(array1[i] + array2[i] )
        except IndexError:
            if len(array1) > len(array2):
                answer.append(array1[i])
            else:
                answer.append(array2[i])
        except:
            print("An Error has occured")
    return answer

