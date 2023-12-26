num=int(input("enter the range number:"))
for x in range(1,num+1):
    c=0
    for y in range(1,x+1):
        if x%y == 0:
            c = c + 1
    if c == 2:
        print(x,"it is prime ")
    else:
        print(x,"not prime")
