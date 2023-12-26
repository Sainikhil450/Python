num=int(input("enter the range:"))
for i in range(1,10+1):
    for j in range(1,num+1):
        print(j,"*",i,"==",j*i,end="   ")
    print()