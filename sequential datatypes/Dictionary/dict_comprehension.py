d={}
for i in range(1,6):
    print(i,end=" == ")
    print(i**3)
    d[i]=i**3
print(d)
print("***********************")
dic1={x:x**3 for x in range(1,6)}
print(dic1)