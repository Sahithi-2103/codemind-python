a=int(input())
b=list(map(int,input().split()))
s=0
c=0
for i in range(len(b)):
    if i%2==0:
        s+=b[i]
    elif i%2!=0:
        c+=b[i]
print(abs(s-c))