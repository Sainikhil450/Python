d1={"b":"blue","c":"car","y":"yellow"}
d2={'a':100,'x':200,"p":"python"}
print(d1)
print(d2)
print("****************************************")

d1.update(d2)
print(d1)
print(d2)

print("**********************")
d1={"b":"blue","c":"car","y":"yellow"}
d2={'a':100,'x':200,"p":"python"}
d2.update(d1)
print(d2)
print(d1)