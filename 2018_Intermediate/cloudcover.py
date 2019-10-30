#Cloud Cover
f = open("cloudin.txt","r")
distList = f.readlines()
f.close()

parameters = distList.pop(0)
distList = [int(i) for i in distList]
(N,K) = [int(i) for i in parameters.split(" ")]

minDist = sum(distList[0:K])
oldDist = minDist

for i in range(N-1-K):
    newDist = oldDist-distList[i]+distList[i+K]
    if newDist < minDist:
        minDist = newDist
    oldDist = newDist

minDist = str(minDist)

f = open("cloudout.txt","w")
f.write(minDist)
f.close()
