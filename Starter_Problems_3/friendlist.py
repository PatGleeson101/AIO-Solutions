Friends = {}
Most = []
with open("listin.txt","r") as f:
    L = int(f.readline())
    for x in range(L):
        a = f.readline().split()
        Friends[a[0]] = Friends.get(a[0],0) +1
        Friends[a[1]] = Friends.get(a[1],0) +1

p = max(Friends.values())
Most = [int(user) for user, frequency in Friends.items() if frequency == p]
Most.sort()
f = open("listout.txt","w")
f.write('\n'.join(str(i) for i in Most))
f.close()
