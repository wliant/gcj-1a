from collections import defaultdict
from collections import OrderedDict

def solveOne(n):
    return [(i, n//i) for i in range(2, int(n**0.5) + 1) if n % i == 0]

def solve(l, secret):
    primeSet = set()
    result = []
    p1,p2 = solveOne(secret[0])[0]
    result.append((p1,p2))
    primeSet.add(p1)
    primeSet.add(p2)

    for i in range(1, len(secret)):
        if secret[i] % p1 == 0:
            p2 = secret[i] / p1
        else:
            p1 = secret[i] / p2
        result.append((p1,p2))
        primeSet.add(p1)
        primeSet.add(p2)
    
    primeSet = sorted(primeSet)
    usedPrimes = {}
    init = 'A'
    for d in primeSet:
        usedPrimes[d] = init
        init = chr(ord(init)+1)  

    init = result[0]
    for i in range(1, len(result)):
        if result[i] != init:  
            start = i
            break
    
    output = ""
    
    if result[i][0] in result[i-1]:
        head = result[i][0]
        tail = result[i][1]
    else:
        head = result[i][1]
        tail = result[i][0]

    
    output = usedPrimes[head] + usedPrimes[tail]

    ite = start - 1
    while ite >= 0:
        temptail = head
        if result[ite][0] == head:
            head = result[ite][1]
        else:
            head = result[ite][0]
        ite -= 1
        output = usedPrimes[head] + output

    ite = start+1
    while ite < len(result):
        temphead = tail
        if result[ite][0] == tail:
            tail = result[ite][1]
        else:
            tail = result[ite][0]
        ite += 1
        output += usedPrimes[tail]

    return output

def printSolution(case, sol):
    print "Case #{0}: {1}".format(case+1, sol)

t = int(raw_input())

for tc in range(t):
    n, l = map(int, raw_input().strip().split(" "))
    secret = map(int, raw_input().strip().split(" "))

    printSolution(tc, solve(l, secret))