d1={"b":"blue","c":"car","y":"yellow"}
d2={'a':100,'x':200,"p":"python"}
print(d1)
print(d2)
print(d1.items())

print("*************************************")

for i in d1.values():
    print(i)
for k in d1.items():
    print(k)
for x,y in d1.items():
    print(x)
    print(y)
#only take d1 means get only key values
for j in d1:
    print(j)