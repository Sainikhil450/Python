#copy---->1.reference copy
d1={"b":"blue","c":"car","y":"yellow"}
print(d1)
print(id(d1))
print("***********************************")
d2=d1
print(d2)
print(id(d2))
print("************************************")
d2["a"]="apple"
print(d2)
print(d1)

