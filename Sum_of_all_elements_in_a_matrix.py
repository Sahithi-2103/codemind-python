a,b=map(int,input().split())
c=[]
for i in range(a):
    inner_list=list(map(int,input().split()))
    c.append(inner_list)
s=0
for inner_list in c:
    for j in inner_list:
        s+=j
print(s)