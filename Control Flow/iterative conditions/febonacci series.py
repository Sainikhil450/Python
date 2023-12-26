num=int(input("enter number:"))
n1,n2=0,1
count=1
if num<=0:
    print("enter positive number")
else:
    while count<=num:
        print(n1)
        res=n1+n2
        n1=n2
        n2=res
        count=count+1