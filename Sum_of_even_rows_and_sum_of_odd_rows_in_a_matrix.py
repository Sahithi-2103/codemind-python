r,c=map(int,input().split())
mat=[]
for inner_list in range(r):
    inner_list = list(map(int,input().split()))
    mat.append(inner_list)
s=0
s1=0
#Element based accessing
for i in range(r):
    for j in range(c):
        if i%2==0:
            s+=mat[i][j]
        else:
            s1+=mat[i][j]
print(s,s1)