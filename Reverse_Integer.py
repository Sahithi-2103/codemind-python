n=int(input())
if n<0:
    temp=-n
else:
    temp=n
rev=0
while temp:
    rev=rev*10+temp%10
    temp=temp//10
if n<0:
    print(-rev)
else:
    print(rev)