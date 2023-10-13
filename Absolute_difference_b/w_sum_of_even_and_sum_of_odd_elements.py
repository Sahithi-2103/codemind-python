a=int(input())
b=list(map(int,input().split()))
s=0
c=0
for i in b:
    if i%2==0:
        s+=i
    elif i%2!=0:
        c+=i
print(abs(s-c))