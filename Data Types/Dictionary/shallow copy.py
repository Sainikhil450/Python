#shallow copy
d1={"b":"blue","c":"car","y":"yellow"}
print(d1)
print(id(d1))
d2=d1.copy()
print(d2)
print(id(d2))