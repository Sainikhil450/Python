d1={"b":"blue","c":"car","y":"yellow","r":"red"}
print(d1)
#delete
del d1["c"]
print(d1)

print("**********************************")
#pop
d1.pop("b")
print(d1)

print("**************************************")
d1.pop("r")
print(d1)

print("***************************************")
#popitem
d1["a"]="apple"
d1["k"]="king"
print(d1)
d1.popitem()
print(d1)

d1.popitem()
print(d1)