fileA = open("MP11data1.txt")
lstA=[]
line=fileA.readline()
while line:
    lineA=float(line.strip())
    lstA.append(lineA)
    line=fileA.readline()
fileA.close()

fileB = open("MP11data2.txt")
lstB=[]
line=fileB.readline()
while line:
    lineB=float(line.strip())
    lstB.append(lineB)
    line=fileB.readline()
fileB.close()


numA=0
numB=0

while numA < len(lstA) and numB < len(lstB):
    if lstA[numA] >= lstB[numB]:
        print(lstA[numA])
        numA += 1
    elif lstA[numA] < lstB[numB]:
        print(lstB[numB])
        numB += 1

if numA >= len(lstA):
    for i in range(len(lstB)-numB):
        print(lstB[numB])
        numB +=1
elif numB <= len(lstB):
    for i in range(len(lstA)-numA):
        print(lstA[numA])
        numA +=1


    
