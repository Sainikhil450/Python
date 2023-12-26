d1={"b":"blue","c":"car","y":"yellow"}
d2={'a':100,'x':200,"p":"python"}
for i in d1.items():
    print(i)
    for j in d2.items():
        print(j)
print("*******************************")

for k in d1,d2:
    print(k)