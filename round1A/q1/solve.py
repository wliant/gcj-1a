#!/bin/python3


def solve(wlist):
    return 0

def printSolution(case, sol):
    print("Case #{0}: {1}".format(case+1, sol))

t = int(input())

for tc in range(t):
    n = str(input())
    w = []
    for l in range(n):
        w.append(input().strip())

    printSolution(tc, solve(w))
