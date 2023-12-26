num=int(input("enter:"))
n1,n2=0,1
print(n1)
print(n2)
for i in range(1,num-1):
    res=n1+n2
    print(res)
    n1=n2
    n2=res

