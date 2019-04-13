primeList = []

with open("prime.txt") as infile:
    for line in infile:
        primeList += map(int, line.strip().split("\t"))
with open("prime2.txt") as infile:
    for line in infile:
        primeList += map(int, line.strip().split("\t"))
with open("prime3.txt") as infile:
    for line in infile:
        primeList += map(int, line.strip().split("\t"))

with open("myPrime.txt", 'w') as outfile:
    outfile.write(str(primeList))