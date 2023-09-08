n=int(input())
q=n
max=0
while q!=0:
    r=q%10
    if r>max:
        max=r
    q=q//10
print(max)