m,n=map(int,input().split())
mat=[]
for i in range(m):
    inner_list=list(map(int,input().split()))[:n:]
    mat.append(inner_list)
s=0
s1=0
for inner_list in mat:
    for every_value in inner_list:
        if every_value%2==0:        
            s+=every_value
        else:
            s1+=every_value
print(f"{s} {s1}")