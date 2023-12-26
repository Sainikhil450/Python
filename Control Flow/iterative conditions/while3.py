i=1
s=0
c=0
m=1
while i<=100:
    if i%2==0:
        print(i)
        s=s+i
        c=c+1
        m=m*i
    i=i+1
print("----------------------")
print(s)
print(c)
print(m)