#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the countingValleys function below.
def countingValleys(n, s):
    step_val = 0
    num_valleys = 0
    if n>1 and n<=1e6:
        for letter in s:
            if letter == 'D':
                step_val -= 1
            elif letter == 'U':
                step_val += 1
            
            if step_val == 0:
                num_valleys += 0.5
    
    return int(num_valleys)
            



if __name__ == '__main__':
    dirpath = os.getcwd()
    folder = 'counting_valleys'
    fptr = open(dirpath+'/'+folder+'/output.txt', 'w')

    n = int(input())

    s = input()

    result = countingValleys(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()
