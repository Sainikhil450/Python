s=0
c=0
m=1
for i in range(1,10):
    if i%2==0:
        print(i)
        s=s+i
        c=c+1
        m=m*i
print("sum:",s)
print("count:",c)
print("product:",m)
