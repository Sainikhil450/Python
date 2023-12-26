d1={"b":"blue","c":"car","y":"yellow"}
d2={'a':100,'x':200,"p":"python"}
d3={}
d3.update(d2)
print(d3)
d3.update(d1)
print(d3)

print("******************************************")

d4={}
for x in d1,d2:
    d4.update(x)
    print(d4)

print("********************************************")

