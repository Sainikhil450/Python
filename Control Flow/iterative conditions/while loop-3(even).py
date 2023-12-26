x=1
s=0
while x<=20:
    if x%2==0:
        print(x,"is even number")
        s=s+x
    else:
        print(x,"is odd number")

    x=x+1
print("---------")
print(s)