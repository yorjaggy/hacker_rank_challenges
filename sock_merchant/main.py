#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    temp_res = {}
    counter = 0
    if (n>0 and n<101):
        #Store all in one dict, avoiding repetitions
        for i in ar:
            if i>0 and i<101:
                if i not in temp_res:
                    temp_res[i] = 1
                else:
                    temp_res[i] += 1

        # verify with module if its a odd number
        for i in temp_res:
                counter+=int(temp_res[i]/2)
    
    # return results
    return counter

if __name__ == '__main__':
    dirpath = os.getcwd()
    fptr = open(dirpath+'/sock_merchant/output.txt', 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
