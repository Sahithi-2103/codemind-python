m=int(input())
n=int(input())
a=0
b=0
for i in range(1,m):
    if m%i==0:
        a+=i
for j in range(1,n):
    if n%j==0:
        b+=j
if (a==n and b==m):
    print("Amicable")
else:
    print("Not Amicable")