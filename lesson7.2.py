N = int(input()) 
n = list(map(int,input().split()))
s = []

for i in range(len(n)):
    if n[i] <= 100000:
        s.append(n[i])
if len(n) > 10e9:
    print("False")

s.insert(0, s.pop())
print(s)