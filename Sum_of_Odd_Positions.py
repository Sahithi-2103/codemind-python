x=int(input())
n=list(map(int,input().split()))
s=0
for i in range(len(n)):
    if i%2!=0:
        s+=n[i]
print(s)