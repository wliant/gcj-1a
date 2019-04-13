def solve(num):
    num1 = [0 for i in range(len(num))]
    num2 = [0 for i in range(len(num))]

    remain = 0
    for index, charac in enumerate(num):
        val = int(charac)
        div = (remain*10+val)/2
        num1[index] = div
        if index == len(num) - 1:
            num2[index] = remain*10 + val - div
            nindex = index
            while num2[nindex] >= 10:
                num2[nindex] = 0
                num2[nindex-1]+=1
                nindex -=1
        else:
            num2[index] = div
            if val % 2 != 0:
                remain = 1
            else:
                remain = 0

    index = len(num) - 1
    while index >= 0:
        if num1[index] == 4 and num2[index] == 4:
            num1[index] = 5
            num2[index] = 3
        elif num1[index] == 4 or num2[index] == 4:
            if num1[index] == 9:
                num1[index] = 8
                num2[index] = 5
            elif num2[index] == 9:
                num1[index] = 5
                num2[index] = 8
            elif num1[index] == 0:
                num1[index] = 1
                num2[index] = 3
            elif num2[index] == 0:
                num1[index] = 3
                num2[index] = 1
            elif num1[index] == 3:
                num1[index] = 2
                num2[index] = 5
            elif num2[index] == 3:
                num1[index] = 5
                num2[index] = 2
            elif num1[index] == 4:
                num1[index] = 3
                num2[index] +=1
            else:
                num1[index] +=1
                num2[index] = 3
        index -=1
    if num1[0] == 0 and len(num1) > 1:
        num1 = num1[1:]
    if num2[0] == 0 and len(num2) > 1:
        num2 = num2[1:]
    return ["".join(map(str, num1)), "".join(map(str,num2))]

def printSolution(case, sol):
    print "Case #{0}: {1} {2}".format(case+1, sol[0], sol[1])

t = int(input())

for tc in range(t):
    v = str(input())
    printSolution(tc, solve(v))