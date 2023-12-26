num=int(input("enter the number:"))
sum=0
r=len(str(num))

temp=num
while temp>0:
    digit=temp%10
    sum+=digit**r
    temp=temp//10
if num==sum:
    print("it is amstrong number")
else:
    print("it is not amstrong number")

