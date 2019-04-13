#!/bin/python3

import math
import os
import random
import re
import sys

def findPair(n):
    print(n)
    a = 0
    b = n
    i = 0
    while(n > 0):
        m = n % 10;
        n = int(n / 10);

        if (m < 2):
            if (n > 0):
                a += (5 *(10 ** i))
                n -= 1
        elif(m == 2 or m == 4 or m == 6):
            a += (10 ** i)
        else:
            a += (2 *(10 ** i))            
        i += 1
    print(a, b-a)
    return a, b-a
            
    


if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        n = int(input())

        findPair(n)
