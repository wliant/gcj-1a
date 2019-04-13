#!/bin/python3

import math
import os
import random
import re
import sys

from functools import reduce

def factors(n):    
    return set(reduce(list.__add__, 
                ([i, n//i] for i in range(2, int(n**0.5) + 1) if n % i == 0)))


def decrypt(n, l, cipher, case):
    r = ""
    primes = []
    encrypted = []
    cipher = list(map(int, cipher.split(" ")))
    f1 = factors(cipher[0])
    #print(f1)
    for c in range(1, len(cipher)):
        f2 = factors(cipher[c])
        #print(f2)
        first = f1 - f2
        if first:
            first = list(first)[0]
            if first <= n:
                if first not in encrypted or encrypted[len(encrypted) - 1] != first:
                    encrypted.append(first)            
                if first not in primes:
                    primes.append(first)

        second = f1.intersection(f2)
        if second:
            second = list(second)[0]        
            if second <= n:
                encrypted.append(second)
                if second not in primes:
                    primes.append(second)

        if (c == len(cipher) -1):
            last = f2 - f1
            if last:
                last = list(last)[0]
                encrypted.append(last)            
                if last not in primes:
                    primes.append(last)
            else:
                if second <= n:
                    encrypted.append(second)                

        f1 = f2
    

    #print(primes)
    primes.sort()
    #print(primes[0:26])
    #print(encrypted)

    chars_map = {}
    char = 'A'
    for num in primes[0:26]:
        chars_map[num] = char
        char = chr(ord(char) + 1)

    for e in encrypted:
        r += chars_map[e]

    #print(len(r), l)
    
    print("Case #{0}: {1}".format(case+1, r))
            
    


if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        s = raw_input().strip().split(" ")
        n = int(s[0])
        l = int(s[1])
        
        cipher = raw_input().strip()

        decrypt(n,l,cipher,t_itr)
