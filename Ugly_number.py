n=int(input())
q=n
c=0
if(q>0):
    while(q!=0):
        if(q%2==0):
            q=q/2
        elif(q%3==0):
            q=q/3
        elif(q%5==0):
            q=q/5
        else:
            c+=1
            break
    if(c==1):
        if(q==1):
            print("Ugly Number")
        else:
            print("Not Ugly Number")
    else:
        print("Ugly Number")
else:
    print("Not Ugly Number")