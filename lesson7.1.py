N = list (map(int,input().split()))
n = []

for i in range(len(N)):
    if N[i] <= 10e5:
        n.append(N[i]) 
        if len(N) > 10000:
            print ("End")
n.reverse()           
print (n)