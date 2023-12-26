x=int(input("enter the number: "))
c=0
i=1
while i<=x:
    if x%i==0:
        c=c+1

    i=i+1
if c==2:
    print(x,"prime number")
else:
    print(x,"not prime number")
