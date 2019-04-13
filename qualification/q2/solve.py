def getLinear(n, x, y):
    return (y-1) * n + x
def buildMap(n, v):
    result = {}
    currentX = 1
    currentY = 1
    for step in v:
        prevX = currentX
        prevY = currentY

        if step == "S":
            currentY +=1
        if step == "E":
            currentX +=1
        
        fromVal = getLinear(n, prevX, prevY)
        toVal = getLinear(n, currentX, currentY)

        result[fromVal] = toVal
    return result


def solve(n, v):
    built = buildMap(n, v)

    result = ""
    currentX = 1
    currentY = 1
    for i in range(n - 1):
        currentX = i+1
        currentY = i+1
        current = getLinear(n, currentX, currentY)
        if_ES = [getLinear(n, currentX + 1, currentY), getLinear(n, currentX+1, currentY + 1)]
        if_SE = [getLinear(n, currentX, currentY+1), getLinear(n, currentX+1, currentY + 1)]

        if current in built:
            val = built[current]
            if val == if_ES[0]:
                result+= "SE"
            else:
                result += "ES"
        else:
            if if_ES[0] in built and built[if_ES[0]] == if_ES[1]:
                result+= "SE"
            else:
                result += "ES"
    return result



def printSolution(case, sol):
    print "Case #{0}: {1}".format(case+1, sol)

t = int(raw_input())

for tc in range(t):
    n = int(raw_input())
    v = str(raw_input())
    printSolution(tc, solve(n, v))