a=int(input())
b=list(map(int,input().split()))
c=int(input())
d=0
for i in range(len(b)):
    if b[i]>d:
        d=b[i]
    if b[i]+c>=d:
        print("True",end=" ")
    else:
        print("False",end=" ")