#!/bin/python3


def solve(wlist):
    levels=[]
    tree = {}
    
    
    for word in wlist:
        currentNode = tree
        i = len(word) - 1
        while i >= 0:
            c = word[i]
            if c in currentNode:
                currentNode = tree[c]
            else:
                currentNode[c] = {}
            i -=1
    
    print(tree)


def printSolution(case, sol):
    print("Case #{0}: {1}".format(case+1, sol))

t = int(input())

for tc in range(t):
    n = int(input())
    w = []
    for l in range(n):
        w.append(input().strip())

    printSolution(tc, solve(w))
