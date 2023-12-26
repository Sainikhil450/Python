d1={"b":"blue","c":"car","y":"yellow"}
d2={'a':100,'x':200,"p":"python"}
print(d1)
r=d1["y"]
print(r)

print("*********************************")

res=d1.get("y","no key")
print(res)
print(d1)
res1=d1.setdefault("z","no key")
print(res1)
print(d1)