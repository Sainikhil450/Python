n=int(input("enter the range of number:"))
x=2
while x<=n:
    i=1
    c=0
    while i<=x:
        if x%i==0:
            c=c+1
        i=i+1
    if c==2:
        print(x,"is prime number")
    else :
        print(x,"is not prime number")
    x=x+1

1